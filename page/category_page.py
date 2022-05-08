from base.page_base import BaseClass
from selenium.webdriver.common.by import By
from base import data

class AmazonCategoryPage(BaseClass):
    """AmazonCategoryPage is from the search results displayed, click on the 2nd page and go to the 3rd product."""

    SECOND_PAGE = (By.CSS_SELECTOR, "a[aria-label='Go to page 2']")
    THIRD_PRODUCT = (By.CSS_SELECTOR, "[data-component-type='s-product-image'] > a")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[cel_widget_id*='MAIN-SEARCH'] h2")
    SEARCH_TEXT_ELEMENT = (By.CSS_SELECTOR, "[data-component-type='s-result-info-bar'] span")
    SELECT_PAGINATION = (By.CLASS_NAME, "s-pagination-selected")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def is_correct_search(self):
        """Returns search result validation for assert"""
        return self.presence_for_all_elements(self.SEARCH_TEXT_ELEMENT)[2].text.strip('"') == data.search_keyword

    def click_second_page(self):
        """Clicks second page on search results"""
        self.presence_for_element(self.SECOND_PAGE).click()

    def is_on_second_page(self):
        """Checks and returns that we are page 2 for the assert"""
        return self.presence_for_element(self.SELECT_PAGINATION).text == "2"

    def click_third_product(self):
        """Clicks third product on search results"""
        self.presence_for_all_elements(self.THIRD_PRODUCT)[2].click()
