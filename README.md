# Parking Lot Ticketing System

A small working prototype of automated parking lot ticketing system

## Purpose
We want to build a small parking lot that will issue tickets to the cars with relevant details.

## Features
* Issue tickets to the driver, ticket containing the slot number and car features - Color and registration number.
* Find registration numbers of all cars of a particular color.
* Find Slot number in which a car with a given registration number is parked. 
* Find Slot numbers of all slots where a car of a particular colour is parked.


## How to setup and run tests/lint

Make sure python3.7 is installed and added to path.
    
    python --version
    
or

    python3.7 --version

Then create a virtual environment for the project.

    virtualenv -p python venv
    . venv/bin/activate
    
or

    virtualenv -p python3.7 venv
    . venv/bin/activate



Then on all platforms install the python dependencies:

    pip install -r requirements.txt

Optionally install the pre-commit hook by copying the following into .git/hooks/pre-commit

    #!/bin/sh
    git-pylint-commit-hook
    
Save the file and make it executable

    chmod +x .git/hooks/pre-commit
    
Note the above two steps can be ignored as we already have linter/pylint setup in our project as explained below.

Run tests:

    python -m unittest

Run Linting:

    sh scripts/lint.sh
    
The above command will run the shell script to run linting on the complete code base to check for PEP8 errors, bugs, stylic inconsistencies as per the python standards. The project uses a healthy combination of different linting tools (pylint, flake8 and so) to get the better results and generates the report. Our goal is to make the code base (both src and tests) 100% lint approved.

After successful execution of the above shell script, Run

    echo $?
It will check the exit code of the last command. If the output is 0 (zero), the linting has passed successfully. If the output is non-zero integer, it indicates there are some linting issues which can be found in the generated report and can be fixed accordingly.

#### Validating the app
The validation of the app can be done by running unit tests which covers all the features
or

via command line interface

cd into root directory of the project and run the app.

    python src/app.py
    
You will get the following prompt:

    Welcome to automated Parking Ticketing System !!
    Type the commands and press Enter to interact. To exit anytime, just Press Enter
    
The different commands can be proided to validate the app.
     