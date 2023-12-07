"""Steps related to browser control on the project app page."""
import time

from behave import *

from pom.locators import Locators


@when("Navigate to project homepage")
def step_impl(context):
    """
    Navigate to project homepage which is defined in the locators.py file
    as the HOME_PAGE constant.
    :type context: behave.runner.Context
    """
    context.browser.get(Locators.HOME_PAGE)


@step("Wait for {num:d} seconds")
def step_impl(context, num):
    """
    Utility method to wait for the specified amount of seconds for visual verification.
    :param num: amount of seconds to wait
    :type context: behave.runner.Context
    """
    time.sleep(num)


@step("I search for user using search button")
def step_impl(context):
    """
    Searches for username from `context.table`.
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    user_name = eval(var_name)

    context.search_field_element.search_for_user(user_name)


@step("Refresh the page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.refresh()
