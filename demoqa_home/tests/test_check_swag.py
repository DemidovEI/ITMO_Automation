from pages.swag_labs import SwagLabs


def test_icon(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_icon()


def test_name(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_name()

def test_password(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_password()
