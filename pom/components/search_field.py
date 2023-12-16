"""Module for SearchField class."""
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec

from pom.components.base_element import BaseElement
from pom.locators import Locators


class SearchField(BaseElement):
    """Class representing Search Field component."""

    def search_for_user_with_click(self, user_name):
        """Method that enters `user_name` into search field and clicks the search button."""
        self.find_visible_element(Locators.SEARCH_FIELD).send_keys(user_name)
        self.click(Locators.SEARCH_BUTTON)

    def search_for_user_with_key(self, user_name):
        """Method that enters `user_name` into search field and presses the Return key."""
        element = self.find_visible_element(Locators.SEARCH_FIELD)
        element.send_keys(user_name)
        element.send_keys(Keys.RETURN)

    def check_empty_search_results(self):
        """Method that checks empty search results"""
        try:
            self.wait.until_not(ec.presence_of_element_located(Locators.SEARCH_RESULTS))
        except TimeoutException:
            print("Search results are not empty. Test failed.")
