"""Module with a single class to store locators and some string constants for the project."""
from selenium.webdriver.common.by import By


class Locators:
    """Class that contains locators, endpoints and other string constants
       for the GitHub Search project."""

    # Project home page
    HOME_PAGE = "https://gh-users-search.netlify.app/"

    # Search Field component
    SEARCH_FIELD = (By.XPATH, "//input[@data-testid='search-bar']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    # User Info component
    FULL_NAME = (By.XPATH, "//article[contains(@class,'sc-dkrFOg')]//header//h4")
    TWITTER = (By.XPATH, "//article[contains(@class,'sc-dkrFOg')]//header//p")
    FOLLOW_BUTTON = (By.XPATH, "//article[contains(@class,'sc-dkrFOg')]//header//a")
    BIO = (By.XPATH, "//article[contains(@class,'sc-dkrFOg')]//p[@class='bio']")
    COMPANY = (By.XPATH, "//article[contains(@class,'sc-dkrFOg')]//div[@class='links']/p[1]")
    LOCATION = (By.XPATH, "//article[contains(@class,'sc-dkrFOg')]//div[@class='links']/p[2]")
    BLOG = (By.XPATH, "//article[contains(@class,'sc-dkrFOg')]//div[@class='links']/a")

    # Followers component
    FOLLOWERS_CONTAINER = (By.XPATH, "//div[@class='followers']")
    FOLLOWER_ENTRY = (By.XPATH, "//div[@class='followers']/article")

    # GitHub API endpoints
    GITHUB_HOMEPAGE = "https://github.com/"
    GITHUB_API_USERS = "https://api.github.com/users/"
    GITHUB_API_AUTH_USER = "https://api.github.com/user"
