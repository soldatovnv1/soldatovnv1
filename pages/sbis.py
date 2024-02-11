from selenium.webdriver.common.by import By
from pages.base_page import BasePage

contact_selector = (By.CSS_SELECTOR, "[href='/contacts']")

class sbis_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def contact(self):
        return self.find(contact_selector)
    def open(self):
        self.browser.get("https://sbis.ru/")

