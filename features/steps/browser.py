"""Steps related to browser control on the project app page."""
import time

from behave import step

from pom.locators import Locators
from pom.components.user_info import UserInfo
from pom.components.search_field import SearchField
from pom.components.user_followers import Followers


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


@step("I search for user using Search Button")
def step_impl(context):
    """
    Searches for username from `context.table`. Waits for the follow button link update.
    :type context: behave.runner.Context
    """
    var_name = "context." + context.table.headings[0]
    user_name = eval(var_name)

    SearchField(context).search_for_user_with_click(user_name)

    # Our condition to verify that User Info has been found and displayed - Follow Button link
    expected_link = Locators.GITHUB_HOMEPAGE + user_name
    UserInfo(context).wait_for_the_fb_link_to_be(expected_link)


@step("I search for user using Enter Key")
def step_impl(context):
    """
    Searches for username from `context.table`. Waits for the follow button link update.
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    user_name = eval(var_name)

    context.search_field_element.search_for_user_with_key(user_name)

    expected_link = Locators.GITHUB_HOMEPAGE + user_name
    context.user_info_element.wait_for_the_fb_link_to_be(expected_link)


@step("I search an empty value")
def step_impl(context):
    """Searches for an empty value
    :type context: behave.runner.Context
    """
    context.search_field_element.search_for_user_with_key("   ")
    context.search_field_element.check_empty_search_results()


@step("I search for not existing user using Enter Key")
def step_impl(context):
    """Searches for non-existing username from `context.table`
    :type context: behave.runner.Context
    """
    var_name = context.table.headings[0]
    user_name = eval(var_name)

    context.search_field_element.search_for_user_with_key(user_name)
    context.search_field_element.check_empty_search_results()


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
    var_name = "context." + context.table.headings[0]
    user_name = eval(var_name)

    expected_link = Locators.GITHUB_HOMEPAGE + user_name
    UserInfo(context).wait_for_the_fb_link_to_be(expected_link)

    assert (UserInfo(context)
            .verify_link_opens_correct_page(Locators.FOLLOW_BUTTON, expected_link) is True), \
        f"Follow link opens wrong page that doesn't contain {expected_link}"


@step("Blog link should redirect to the displayed URL")
def step_impl(context):
    """
    Check that the blog link redirects to displayed URL.
    :type context: behave.runner.Context
    """
    expected_link = UserInfo(context).get_element_text(Locators.BLOG)
    if expected_link.startswith("www."):
        expected_link = expected_link[4:]

    assert (UserInfo(context)
            .verify_link_opens_correct_page(Locators.BLOG, expected_link) is True), \
        f"Blog link opens wrong page that doesn't contain {expected_link}"


@step("I verify followers list length matches saved data")
def step_impl(context):
    """
    :param context: the context object that contains the information for the step implementation
    :return: None

    This step verifies that the length of the followers list matches the length of the saved data.
    It retrieves the saved data from the context object and then retrieves the length of
    the followers list from the user_followers_element.
    If the lengths don't match, an assertion error is raised with an appropriate error message.
    """
    var_name = "context." + context.table.headings[0]
    response = eval(var_name)

    if not Followers(context).is_followers_list_empty():
        followers_list_len = Followers(context).get_followers_list_length()
    else:
        followers_list_len = 0

    saved_data_len = len(response.json())

    message = f"Followers list length: {followers_list_len}. Saved data: {saved_data_len}."
    print(message)

    assert followers_list_len == len(response.json()), f"Mismatch found. {message}"


@step("I verify every follower in the list has a proper GitHub username and profile link")
def step_impl(context):
    """
    :param context: The Behave context object.
    :return: None

    This method verifies that every follower in the list has a username/profile pair that \
    matches with GitHub API data.
    """
    var_name = "context." + context.table.headings[0]
    response = eval(var_name)

    followers_list = Followers(context).get_followers()

    logger = []
    username = ""
    profile_link = ""
    for i, (k, v) in enumerate(followers_list.items()):
        try:
            username = response.json()[i]['login']
            profile_link = response.json()[i]['html_url']
            assert k.lower() == username.lower()
            assert v == profile_link
        except AssertionError:
            message = f"Mismatch in Followers. API: {username.lower()} - {profile_link}. UI: {k.lower()} - {v}."
            logger.append(message)

    if logger:
        raise AssertionError("\n".join(logger))


@step("I verify user {status_str} listed in the Followers component")
def step_impl(context, status_str):
    """
    :param context: The context object that holds information shared across steps
    :param status_str: The status string indicating whether the user should be listed \
    in followers or not
    :return: None

    This step verifies if a user "is"/"is not" listed in the Followers component. \
    Raises a ValueError for any other invalid status string.
    """
    var_name = "context." + context.table.headings[0]
    user_name = eval(var_name)

    match status_str:
        case "is":
            status = True
        case "is not":
            status = False
        case _:
            raise ValueError(f"Invalid verification status: '{status_str}'.")

    followers_list = Followers(context).get_followers()

    for v in followers_list.values():
        if v == Locators.GITHUB_HOMEPAGE + user_name:
            found = True
            break
    else:
        found = False

    assert status is found, \
        f"Expected user to be in the Followers list: '{status}'. Actual: '{found}'."
