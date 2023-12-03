from behave import fixture, use_fixture
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait

# -- CONFIG
IS_MAXIMIZED = True
IMPLICIT_WAIT = 0.0
EXPLICIT_WAIT = 5


@fixture
def browser_chrome(context):
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
    use_fixture(browser_chrome, context)
    context.wait = WebDriverWait(context.browser, EXPLICIT_WAIT)
    # -- CLEANUP-FIXTURE is called after after_feature() hook
