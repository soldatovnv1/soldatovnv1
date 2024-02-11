from selenium.webdriver.common.by import By
from pages.base_page import BasePage

banner_selector = (By.CSS_SELECTOR, "[href='https://tensor.ru/']")

class contact_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def banner(self):
        return self.find(banner_selector)

    def open(self):
        self.browser.get("https://sbis.ru/contacts/")
