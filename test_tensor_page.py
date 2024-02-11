from pages.tensor import tensor_page
about = "https://tensor.ru/about"


def test_site(browser):
    tensorr_page = tensor_page(browser)
    tensorr_page.open()

def test_sila_exist(browser):
    tensorr_page = tensor_page(browser)
    tensorr_page.open()
    tensorr_page.sila()

def test_podrobnee_exist(browser):
    tensorr_page = tensor_page(browser)
    tensorr_page.open()
    tensorr_page.sila()
    tensorr_page.podrobnee().click()
    assert tensorr_page.current() == about


