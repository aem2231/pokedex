import pandas as pd

class UserFunctions:
    def __init__(self, data_file="data/user_data.csv"):
        self.data_file = data_file
        self.users_df = pd.read_csv(self.data_file)

    def validate_user(self, username, password):
        # Find the matching user
        valid_user = self.users_df[(self.users_df["Username"] == username)]

        if valid_user.empty:
            return 2  # No such user

        if valid_user["Password"].values[0] == password:
            return 1  # User and password match
        else:
            return 0  # Password is incorrect
