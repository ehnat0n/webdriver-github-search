"""Module for Followers class."""

from selenium.webdriver.common.by import By

from pom.components.base_element import BaseElement
from pom.locators import Locators


class Followers(BaseElement):
    """Class representing Followers component."""

    def is_followers_list_empty(self):
        """
        Checks if the followers list is empty.

        :return: True if the followers list is empty, False otherwise.
        """
        return self.get_element_text(Locators.FOLLOWERS_CONTAINER) == ""

    def get_followers_list_length(self):
        """
        Returns the length of the followers' list.

        :return: The length of the followers' list.
        """
        return len(self.find_visible_elements(Locators.FOLLOWER_ENTRY))

    def get_followers(self):
        """
        Returns a list of follower names and their respective GitHub profile links.

        :return: dictionary with usernames as keys and GitHub profile links as values.
        """
        followers = {}
        for entry in self.find_visible_elements(Locators.FOLLOWER_ENTRY):
            followers[entry.find_element(*(By.XPATH, ".//h4")).text] = \
                entry.find_element(*(By.XPATH, ".//a")).get_attribute("href")

        return followers
