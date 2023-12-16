"""Behave hooks."""
from behave import fixture, use_fixture
from selenium.webdriver import Chrome


# -- CONFIG
IS_MAXIMIZED = True
IMPLICIT_WAIT = 0.0


@fixture
def browser_chrome(context):
    """Fixture for the Chrome browser. Settings are picked up from `CONFIG` constants."""
    # -- BEHAVE-FIXTURE:
    context.browser = Chrome()

    if IS_MAXIMIZED:
        context.browser.maximize_window()
    if IMPLICIT_WAIT:
        context.browser.timeouts.implicit_wait = IMPLICIT_WAIT

    yield context.browser

    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_feature(context, feature):
    """Set up Chrome fixture."""
    use_fixture(browser_chrome, context)

    # -- CLEANUP-FIXTURE is called after after_feature() hook
