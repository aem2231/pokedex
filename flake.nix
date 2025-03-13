{
  description = "Python Nix Flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachSystem [ "x86_64-linux" ] (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
      pythonEnv = pkgs.python311.withPackages (p: with p; [
        pandas
        requests
        tkinter
        python-dotenv
        customtkinter
        pillow
        bcrypt
      ]);
    in {
      devShell = pkgs.mkShell {
        buildInputs = [ pythonEnv ];

        shellHook = ''
          echo "Environment loaded!"
        '';
      };
    });
}
