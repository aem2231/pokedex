from email.message import Message
from pathlib import Path
from typing import Union
import pandas as pd
import smtplib
from dotenv import load_dotenv
import bcrypt
import os
import re
from utils.helper import Helper
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class AccountManager:
    def __init__(self) -> None:

        # Load all environment variables
        load_dotenv()
        self.EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
        self.EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

        self.data_file: Path = Helper.get_user_data_path()
        try:
            self.users_df = pd.read_csv(self.data_file)
        except pd.errors.EmptyDataError:
            # Initialize empty DataFrame
            self.users_df = pd.DataFrame(columns=['Email', 'Username', 'Password',
                                                'Poké1', 'Poké2', 'Poké3', 'Poké4', 'Poké5', 'Poké6'])

    def validate_user(self, username, password) -> int:
        # Find the matching user
        valid_user = self.users_df[(self.users_df["Username"] == username)]

        if valid_user.empty:
            return 2  # No such user

        stored_hash: str = valid_user["Password"].values[0]

        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            return 1
        else:
            return 0

    def validate_signup(self, email, username, password) -> Union[int, None]:
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return 5 # Invalid email

        if email == "":
            return 6
        if username == "":
            return 7
        if password == "":
            return 8

        if self.users_df["Email"].str.contains(email).any():
            return 3 # Email already exists
        elif self.users_df["Username"].str.contains(username).any():
            return 4 # Username already exists
        elif len(password) < 8:
            return 9 # Password too short
        else:
            # Since the email and username are unique, we can create the account and send a confirmation email.
            self.create_account(email, username, password)
            self.send_email(email, username)


    def create_account(self, email, username, password) -> None:
        new_row = {
           'Email': email,
           'Username': username,
           'Password': Helper.hash_password(password),
           'Poké1': '',
           'Poké2': '',
           'Poké3': '',
           'Poké4': '',
           'Poké5': '',
           'Poké6': ''
        }

        # Append the new row to the data frame
        self.users_df = pd.concat([self.users_df, pd.DataFrame([new_row])], ignore_index=True)
        self.users_df.to_csv(self.data_file, index=False)


    def send_email(self, email, username) -> None:
        sender_email = self.EMAIL_USERNAME
        sender_password = self.EMAIL_PASSWORD
        recipient_email = email

        message = MIMEMultipart()
        message["From"] = str(sender_email)
        message["To"] = recipient_email
        message["Subject"] = "Account Confirmation"

        body = "Signup successful! Welcome to our platform, " + username + "!"
        message.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(str(sender_email), str(sender_password))
            server.sendmail(str(sender_email), recipient_email, message.as_string())
        except Exception as e:
            print(f"An error occured :(\n{e}")
        finally:
            server.quit()
