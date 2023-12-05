from pom.components.base_element import BaseElement
from pom.locators import Locators


class SearchField(BaseElement):
    """Class representing Search Field component."""
    def search_for_user(self, user_name):
        """Method that enters `user_name` into search field and clicks the search button."""
        self.find_element(Locators.SEARCH_FIELD).send_keys(user_name)
        self.click(Locators.SEARCH_BUTTON)
