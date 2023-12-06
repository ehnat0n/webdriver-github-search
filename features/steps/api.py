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


@then("Displayed {data_entry} matches API response")
def step_impl(context, data_entry):
    """
    Checks if displayed `data_entry` matches the API response stored in `context.table`.
    :param data_entry: piece of the GitHub user information
    (Full Name, Twitter, Bio, Company Name, Location, Blog)
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    response = eval(var_name)

    data_key = ""
    element_locator = None

    match data_entry:
        case "Full Name":
            data_key = "name"
            element_locator = Locators.FULL_NAME
        case "Twitter":
            data_key = "twitter_username"
            element_locator = Locators.TWITTER
        case "Bio":
            data_key = "bio"
            element_locator = Locators.BIO
        case "Company Name":
            data_key = "company"
            element_locator = Locators.COMPANY
        case "Location":
            data_key = "location"
            element_locator = Locators.LOCATION
        case "Blog":
            data_key = "blog"
            element_locator = Locators.BLOG
        case _:
            print(f"Invalid data entry alias - {data_entry}. \
                  Use Full Name, Twitter, Bio, Company Name, Location, Blog")

    api_data = response.json()[data_key]
    ui_data = context.user_info_element.get_element_text(element_locator)

    assert api_data == ui_data, \
        f"Error comparing UI and API values for {data_entry}. API: {api_data}. UI: {ui_data}"
