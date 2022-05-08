from base.page_base import BaseClass
from selenium.webdriver.common.by import By
from base import data


class AmazonLoginPage(BaseClass):
    """AmazonLoginPage is login with user account"""

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONTINUE_BTN = (By.ID, "continue")
    LOGIN_BTN = (By.ID, "signInSubmit")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def login(self):
        """User logs in with an existing account"""
        self.send_keys(self.EMAIL_INPUT, data.email)
        self.presence_for_element(self.CONTINUE_BTN).click()
        self.send_keys(self.PASSWORD_INPUT, data.password)
        self.presence_for_element(self.LOGIN_BTN).click()
