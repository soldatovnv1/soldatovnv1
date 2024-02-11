from selenium.webdriver.common.by import By
from pages.base_page import BasePage

text_to_find = "Сила в людях"
sila_selector = (By.XPATH, "//*[text()='" + text_to_find + "']")
podrobnee_selectror = (By.CSS_SELECTOR, "[href='/about']")

class tensor_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def sila(self):
        return self.find(sila_selector)
    def open(self):
        self.browser.get("https://tensor.ru/")

    def podrobnee(self):
        return self.find(podrobnee_selectror)

    def current(self):
        return self.browser.current_url