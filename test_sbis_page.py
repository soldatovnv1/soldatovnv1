from pages.sbis import sbis_page


def test_site(browser):
    sbiss_page = sbis_page(browser)
    sbiss_page.open()

def test_contact_exist(browser):
    sbiss_page = sbis_page(browser)
    sbiss_page.open()
    sbiss_page.contact()

def test_click_contact_exist(browser):
    sbiss_page = sbis_page(browser)
    sbiss_page.open()
    sbiss_page.contact().click()
