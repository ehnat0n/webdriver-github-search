from selenium.webdriver.common.by import By


class Locators:
    """Class that contains locators, endpoints and other string constants
       for the GitHub Search project."""

    # Project home page
    HOME_PAGE = "https://gh-users-search.netlify.app/"

    # Search Field component
    SEARCH_FIELD = (By.XPATH, "//input[@data-testid='search-bar']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    # GitHub API endpoints
    GITHUB_API_USERS = "https://api.github.com/users/"
