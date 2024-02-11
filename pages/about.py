from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import wget

text_to_find = "Работаем"
about_selector = (By.XPATH, "//*[text()='" + text_to_find + "']")

images = ['https://tensor.ru/static/resources/TensorRuWasaby/pages/About/resources/images/work1.jpg?x_module=9c2d594de445b0b579a233ef31959e88',
             'https://tensor.ru/static/resources/TensorRuWasaby/pages/About/resources/images/work2.jpg?x_module=9c2d594de445b0b579a233ef31959e88',
              'https://tensor.ru/static/resources/TensorRuWasaby/pages/About/resources/images/work3.jpg?x_module=9c2d594de445b0b579a233ef31959e88',
              'https://tensor.ru/static/resources/TensorRuWasaby/pages/About/resources/images/work4.jpg?x_module=9c2d594de445b0b579a233ef31959e88']

data_images = ("width_max = 0", "width_min = 10 ** 9", "height_max = 0", "height_min = 10 ** 9")

width_max = 0
width_min = 10 ** 9
height_max = 0
height_min = 10 ** 9

class about_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def about(self):
        return self.find(about_selector)

    def open(self):
        self.browser.get("https://tensor.ru/about")

    def download_image(self, image_name):
        return wget.download(image_name)











