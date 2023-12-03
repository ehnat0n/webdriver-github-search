from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self, context):
        self.driver = context.browser
        self.wait = context.wait

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))
