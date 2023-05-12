from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    #elements_page.bth_sidebar_first.click()
    #time.sleep(3)
    #assert elements_page.bth_sidebar_first_textbox.exist()
    assert not elements_page.bth_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.bth_sidebar_first_checkbox.visible()
    elements_page.bth_sidebar_first.click()
    time.sleep(2)
    assert elements_page.bth_sidebar_first_checkbox.visible()

