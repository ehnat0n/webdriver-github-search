# GitHub User Search Test Project

This is a test project for [GitHub User Search](https://gh-users-search.netlify.app/). The goal is to practice API
automation and to explore the dependency between API calls and data populated on UI.

Project is done in BDD style with Behave. Tests are written in Gherkin format.

Following packages are required (see `requirements.txt`):

- selenium
- behave
- requests
- jsonpath-ng

Manual test cases are in `backclog/<component>.feature` files.

Automated test cases are in `features/<component>.feature` files.

## Setup:

1. Clone the project: `git clone git@github.com:ehnat0n/webdriver-github-search.git`
2. Create virtual environment in the project folder: `python -m venv .venv`
3. Activate it: `.venv/bin/activate`
4. Install required packages: `pip install -r requirements.txt`
