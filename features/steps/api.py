"""Steps related to GitHub API requests."""
import json
from pprint import pprint

import requests
from behave import step

from pom.locators import Locators
from utilities import get_data_from_file, get_github_api_headers


@step("I get user info from GitHub API and save it to {var_data}")
def step_impl(context, var_data):
    """
    Method requests data from GitHub API for `user_name` then saves the response object with
    context variable `var_name`.
    :param var_data: name of the context variable that we are going to use to save user data
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    user_name = eval(var_name)

    token = get_data_from_file("secrets/github_token")

    response = requests.get(
        Locators.GITHUB_API_USERS + user_name,
        headers=get_github_api_headers(token),
        timeout=(2, 5)
    )

    list_ = var_data.split(".")
    if list_[0] == "feature":
        context_obj = context.feature
        context_var = list_[1]
    else:
        context_obj = context
        context_var = list_[0]

    setattr(context_obj, context_var, response)


@step("I verify the response code is {code:d}")
def step_impl(context, code):
    """
    Prints the response code from the response object found in the context table.
    Verifies that the response code matches expected `code`.
    :param code: expected response code
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    response = eval(var_name)

    status_code = response.status_code
    print(f"Response status code: {status_code}")
    assert code == status_code, f"Expected code: {code}. Response code: {status_code}."


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


@step("Displayed {data_entry} matches API response")
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
    if api_data is None:
        if data_key == "location":
            api_data = "earth"
        else:
            api_data = ""
    else:
        if data_key == "twitter_username":
            api_data = "@" + api_data

    ui_data = context.user_info_element.get_element_text(element_locator)

    assert api_data == ui_data, \
        f"Error comparing UI and API values for {data_entry}. API: {api_data}. UI: {ui_data}"


@step("I update test user with {data_set} and save the response to {var_response}")
def step_impl(context, data_set, var_response):
    """
    Updates GitHub `user_name` with info from `data_set`.
    :param var_response: variable name for the response object
    :param data_set: data set that we are going to use to update our user
    :type context: behave.runner.Context
    """
    data = json.loads(get_data_from_file("test_data.json"))[data_set]
    token = get_data_from_file("secrets/github_token")

    response = requests.patch(
        Locators.GITHUB_API_AUTH_USER,
        headers=get_github_api_headers(token),
        json=data,
        timeout=(2, 5)
    )

    setattr(context, var_response, response)


@step("I set username as {user_name} and save it to {var_name}")
def step_impl(context, user_name, var_name):
    """
    Setups `user_name` as a test user by saving it to `context.var_name`.
    :param var_name: name of the variable that we are going to use to store `user_name`
    :param user_name: setup username to use in the following steps
    :type context: behave.runner.Context
    """
    setattr(context, var_name, user_name)
