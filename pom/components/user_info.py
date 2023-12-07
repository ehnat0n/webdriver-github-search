"""Module for UserInfo class."""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec

from pom.components.base_element import BaseElement
from pom.locators import Locators


class UserInfo(BaseElement):
    """Class representing User Info component."""

    def wait_for_the_fb_link_to_be(self, expected_link):
        """Method waits for the Follow button match with `expected_link`.
        :param expected_link: expected user's profile link on GitHub"""
        try:
            self.wait.until(lambda d: expected_link ==
                            self.find_visible_element(Locators.FOLLOW_BUTTON)
                            .get_attribute("href"))
        except TimeoutException as exc:
            raise AssertionError(f"Couldn't find expected link: {expected_link}.") from exc

    def verify_link_opens_correct_page(self, locator, expected_link):
        """Method clicks on the `locator` element and verifies that browser loads `expected_link`.
        :param locator: locator for the element that opens `expected_link`
        :param expected_link: supposed to end up on that page"""
        self.click(locator)

        try:
            self.wait.until(ec.url_contains(expected_link))
        except TimeoutException:
            print(f"Current URL: {self.driver.current_url}. Expected: {expected_link}.")
            return False

        return True
