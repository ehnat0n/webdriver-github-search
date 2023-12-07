"""Steps related to browser control on the project app page."""
import time

from behave import step

from pom.locators import Locators


@step("Navigate to project homepage")
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
    Searches for username from `context.table`. Waits for the follow button link update.
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    user_name = eval(var_name)

    context.search_field_element.search_for_user(user_name)

    expected_link = Locators.GITHUB_HOMEPAGE + user_name
    context.user_info_element.wait_for_the_fb_link_to_be(expected_link)


@step("Refresh the page")
def step_impl(context):
    """
    Refreshes the current page.
    :type context: behave.runner.Context
    """
    context.browser.refresh()


@step("Follow button should redirect to the user's GitHub profile")
def step_impl(context):
    """
    Read `username` from `context.table`, make sure Follow Button has appropriate link
    for user's GitHun profile.
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    user_name = eval(var_name)

    expected_link = Locators.GITHUB_HOMEPAGE + user_name
    context.user_info_element.wait_for_the_fb_link_to_be(expected_link)

    assert (context.user_info_element
            .verify_link_opens_correct_page(Locators.FOLLOW_BUTTON, expected_link) is True), \
        f"Follow link opens wrong page that doesn't contain {expected_link}"


@then("Blog link should redirect to the displayed URL")
def step_impl(context):
    """
    Check that the blog link redirects to displayed URL.
    :type context: behave.runner.Context
    """
    expected_link = context.user_info_element.get_element_text(Locators.BLOG)
    if expected_link.startswith("www."):
        expected_link = expected_link[4:]

    assert (context.user_info_element
            .verify_link_opens_correct_page(Locators.BLOG, expected_link) is True), \
        f"Blog link opens wrong page that doesn't contain {expected_link}"
