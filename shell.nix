{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  packages = [
    (pkgs.python3.withPackages(pypkgs: [
      pypkgs.pandas
      pypkgs.requests
      pypkgs.tkinter
      pypkgs.customtkinter
      pypkgs.python-dotenv
      pypkgs.bcrypt
    ]))
  ];
}
