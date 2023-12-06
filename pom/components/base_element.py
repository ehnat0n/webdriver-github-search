from selenium.webdriver.support import expected_conditions as ec


class BaseElement:
    """Base Element class that contains most common methods and aliases for all pom."""
    def __init__(self, context):
        self.driver = context.browser
        self.wait = context.wait

    def click(self, locator):
        """Click on the element with specified locator after explicit wait
        for element being clickable."""
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        """Returns WebElement with specified locator after explicit wait
        for element being visible."""
        return self.wait.until(ec.visibility_of_element_located(locator))

    def find_elements(self, locator):
        """Returns all WebElements with specified locator after explicit wait
        for elements being visible."""
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def get_element_text(self, locator):
        """Returns elements text."""
        return self.find_element(locator).text
