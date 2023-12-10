"""Behave hooks."""
from behave import fixture, use_fixture
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait

from pom.components.search_field import SearchField
from pom.components.user_info import UserInfo

# -- CONFIG
IS_MAXIMIZED = True
IMPLICIT_WAIT = 0.0
EXPLICIT_WAIT = 5


@fixture
def browser_chrome(context):
    """Fixture for the Chrome browser. Settings are picked up from `CONFIG` constants."""
    # -- BEHAVE-FIXTURE:
    context.browser = Chrome()

    if IS_MAXIMIZED:
        context.browser.maximize_window()
    if IMPLICIT_WAIT:
        context.browser.timeouts.implicit_wait = IMPLICIT_WAIT

    context.wait = WebDriverWait(context.browser, EXPLICIT_WAIT)

    yield context.browser

    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_feature(context, feature):
    """Set up Chrome fixture, wait and web app elements for every feature run."""
    use_fixture(browser_chrome, context)

    # Creating instances to work with app components
    context.search_field_element = SearchField(context)
    context.user_info_element = UserInfo(context)

    # -- CLEANUP-FIXTURE is called after after_feature() hook
