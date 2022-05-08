import unittest
from selenium import webdriver
from page.main_page import AmazonMainPage
from page.login_page import AmazonLoginPage
from page.category_page import AmazonCategoryPage
from page.product_page import AmazonProductPage
from page.list_page import AmazonListPage


class AmazonHappyPath(unittest.TestCase):
    website = "https://www.amazon.com/"
    executable_path = "/home/onuryondem/automation/amazon/chromedriver"

    def setUp(self):
        self.driver = webdriver.Chrome(self.executable_path)
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.main_page = AmazonMainPage(self.driver)
        self.login_page = AmazonLoginPage(self.driver)
        self.category_page = AmazonCategoryPage(self.driver)
        self.product_page = AmazonProductPage(self.driver)
        self.list_page = AmazonListPage(self.driver)

    def test_case(self):
        """Test case is:
        1. Go to given website
        2. Go to login page
        3. Login with an existing account
        4. Search for the samsung keyword in the search bar
        5. Go to page 2 on the incoming page
        6. Go to the 3. product
        7. Click the add to list button from the selected product
        8. Click shopping list on the navbar
        9. Delete the product added to the list
        """

        is_on_main_page = self.main_page.is_on_main_page()
        assert is_on_main_page, "We are not on the homepage"
        self.main_page.navigate_to_sign_in_page()
        self.login_page.login()
        self.main_page.search_keywords()
        is_correct_search = self.category_page.is_correct_search()
        assert is_correct_search, "Search result is not correct"
        self.category_page.click_second_page()
        is_on_second_page = self.category_page.is_on_second_page()
        assert is_on_second_page, "Not on page 2"
        self.category_page.click_third_product()
        self.product_page.add_to_list()
        self.product_page.navigate_to_wish_list()
        is_product_on_the_list = self.list_page.is_product_have()
        assert is_product_on_the_list, "The product has not been added to the list"
        self.list_page.delete_favorite_product()
        is_product_deleted = self.list_page.is_deleted_favorite_product()
        assert not is_product_deleted, "The product has not been deleted from the list"

    def tearDown(self):
        self.driver.quit()
