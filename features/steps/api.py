"""Steps related to GitHub API requests."""
from pprint import pprint

import requests
from behave import *

from pom.locators import Locators
from utilities import get_data_from_file, get_github_api_headers


@step("I get user info for {user_name} from GitHub API and save it to {var_name}")
def step_impl(context, user_name, var_name):
    """
    Method requests data from GitHub API for `user_name` then saves the response object with
    context variable `var_name`.
    :param var_name: name of the context variable that we are going to use to save user data
    :param user_name: GitHub username for the GET request
    :type context: behave.runner.Context
    """
    token = get_data_from_file("secrets/github_token")

    response = requests.get(
        Locators.GITHUB_API_USERS + user_name,
        headers=get_github_api_headers(token),
        timeout=(2, 5)
    )

    setattr(context, var_name, response)


@then("I print the response code")
def step_impl(context):
    """
    Prints the response code from the response object found in the context table.
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    response = eval(var_name)
    print(f"Response status code: {response.status_code}")


@step("I print user data")
def step_impl(context):
    """
    Prints the data from the response object found in the context table.
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    print(var_name)
    response = eval(var_name)

    pprint(response.json())
