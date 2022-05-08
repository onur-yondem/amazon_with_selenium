from base.page_base import BaseClass
from selenium.webdriver.common.by import By
from base import data


class AmazonProductPage(BaseClass):
    """AmazonProductPage is adds the product to the wish list and goes to the wish list"""

    ADD_TO_LIST_BTN = (By.ID, "add-to-wishlist-button-submit")
    WISH_LIST_BTN = (By.CSS_SELECTOR, ".nav-panel a")
    ACCOUNT_BTN = (By.CSS_SELECTOR, "a[data-nav-role='signin']")
    WISH_LIST_CONTAINER = (By.CLASS_NAME, "nav-panel")
    VIEW_YOUR_LIST_BTN = (By.ID, "huc-view-your-list-button")
    CLOSE_BTN = (By.CLASS_NAME, "a-button-close")
    PRODUCT_TITLE = (By.ID, "productTitle")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def add_to_list(self):
        """Adds the product to the list and closes the popup"""
        data.product_title = self.presence_for_element(self.PRODUCT_TITLE).text.strip()
        self.presence_for_element(self.ADD_TO_LIST_BTN).click()
        self.presence_for_element(self.VIEW_YOUR_LIST_BTN)
        self.presence_for_element(self.CLOSE_BTN).click()

    def navigate_to_wish_list(self):
        """Goes to list"""
        self.move_to_element(self.ACCOUNT_BTN)
        self.presence_for_element(self.WISH_LIST_CONTAINER)
        self.presence_for_element(self.WISH_LIST_BTN).click()
