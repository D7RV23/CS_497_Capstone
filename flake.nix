{
  description = "Phishing Dataset Loader Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        pythonPackages = pkgs.python311Packages;
      in {
        devShells.default = pkgs.mkShell {
          name = "phishing-email-env";
          # Packages for the flake
          buildInputs = [
            pythonPackages.python
            pythonPackages.pip
            pythonPackages.setuptools
            pythonPackages.wheel
            pythonPackages.datasets 
            pythonPackages.numpy
            pythonPackages.scikit-learn
            pythonPackages.pandas
	          pythonPackages.torch
           #  pythonPackages.cv2
          ];

          shellHook = ''
            figlet WELCOME LUCY
	          figlet Nix environment"
            ls -a 
          '';
        };
      });
}

