# GitHub User Search Test Project
This is a test project for [GitHub User Search](https://gh-users-search.netlify.app/). The goal is to practice API automation and to explore the dependency between API calls and data populated on UI.

Project is done in BDD style with Python and Behave. Tests are written in Gherkin language.

Following packages are required (see `requirements.txt`):

- selenium
- behave
- requests
- jsonpath-ng

Manual test cases are in `backlog/<component>.feature` files.

Automated test cases are in `features/<component>.feature` files.

## Test user data
Test data sets are stored in `test_data.json` file. You can use it with any account that you control. GitHub's authentication token will be required for updates. Code expects it at `secrets/github_token` relative path.

## Setup:
1. Clone the project: `git clone git@github.com:ehnat0n/webdriver-github-search.git`
2. Create virtual environment in the project folder: `python -m venv .venv`
3. Activate it in Linux - `.venv/bin/activate`, or Windows (PowerShell) - `.venv\Scripts\Activate.ps1`
4. Install required packages: `pip install -r requirements.txt`

## Run:
Run in IDE or from console - use `behave .` in project directory
