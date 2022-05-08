from selenium.webdriver.common.by import By
from base.page_base import BaseClass
from base import data


class AmazonMainPage(BaseClass):
    """AmazonMainPage is goes to the login page and searches for products"""

    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a[data-nav-role='signin']")
    SEARCH_INPUT = (By.NAME, "field-keywords")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    MAIN_PAGE_CONTENT = (By.CSS_SELECTOR, "[role='main']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def is_on_main_page(self):
        """Assert for main page"""
        return self.presence_for_element(self.MAIN_PAGE_CONTENT).is_displayed()

    def navigate_to_sign_in_page(self):
        """Clicks login button"""
        self.presence_for_element(self.SIGN_IN_BUTTON).click()

    def search_keywords(self):
        """Searches for keywords via the search bar"""
        self.send_keys(self.SEARCH_INPUT, data.search_keyword)
        self.presence_for_element(self.SEARCH_BTN).click()
