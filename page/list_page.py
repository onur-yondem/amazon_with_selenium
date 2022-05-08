from base.page_base import BaseClass
from selenium.webdriver.common.by import By
from base import data


class AmazonListPage(BaseClass):
    """AmazonListPage is controls the product added to the list and deletes the product"""

    WISH_LIST_ITEMS = (By.CSS_SELECTOR, "a[id*='itemName_']")
    DELETE_BTN = (By.NAME, "submit.deleteItem")
    UNDO = (By.CSS_SELECTOR, "span[data-action='reg-item-delete-undo']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
        self.index = -1

    def is_product_have(self):
        """Checks if the product we add for Assertion is in the list and returns it"""
        for index, item in enumerate(self.presence_for_all_elements(self.WISH_LIST_ITEMS)):

            if data.product_title == item.get_attribute("title"):
                self.index = index
                return data.product_title == item.get_attribute("title")
                break

        return False

    def delete_favorite_product(self):
        """Deletes the product added to the list"""
        self.presence_for_all_elements(self.DELETE_BTN)[self.index].click()

    def is_deleted_favorite_product(self):
        """Checks and returns whether the product has been deleted"""
        if not self.presence_for_element(self.DELETE_BTN).is_displayed():
            for index, item in enumerate(self.presence_for_all_elements(self.WISH_LIST_ITEMS)):

                if data.product_title == item.get_attribute("title"):
                    return data.product_title == item.get_attribute("title")

            return False

