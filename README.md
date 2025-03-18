# Pokedex App

## Overview
Yet another collage project.

## Directory Tree
```
.
├── config
│   └── config.jsonc
├── data
│   ├── pokemon.json
│   └── user_data.csv
├── flake.lock
├── flake.nix
├── README.md
├── requirements.txt
├── REVIEW.md
├── session.json
├── src
│   ├── api
│   │   └── pokemon.py
│   ├── app.py
│   ├── models
│   │   ├── account_manager.py
│   │   ├── home_model.py
│   │   └── search_model.py
│   ├── utils
│   │   ├── error_codes.py
│   │   └── helper.py
│   └── views
│       ├── home_view.py
│       ├── login_view.py
│       ├── search_view.py
│       └── signup_view.py
├── test.py
└── themes
    └── catppuccin-mocha.json
```

## Prerequisites
- Python 3 or higher
- Required packages listed in `requirements.txt`

## Installation

First, clone the repository:
```sh
git clone https://github.com/aem2231/pokedex.git
```

Then cd to the directory you cloned it to:
```sh
cd ~/pokedex
```

### Using pip
To install the required packages using pip, run:
```sh
pip install -r requirements.txt
```

### Using nix
If you have direnv installed, just run:
```sh
direnv allow
```
Otherwise, run:
```sh
nix develop
```

## Running the Code

### On Windows
To run on Windows, use:
```sh
python src\app.py
```

### On Linux
To run on Linux, use:
```sh
python3 src/app.py
```
