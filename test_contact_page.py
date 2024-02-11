from pages.contacts import contact_page


def test_banner_exist(browser):
    contactt_page = contact_page(browser)
    contactt_page.open()
    contactt_page.banner().click()

