from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_text_footer(browser):
    page = Demoqa(browser)
    page.visit()
    footer_text = page.footer.get_text()
    assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_text_element(browser):
    page = Demoqa(browser)
    page.visit()
    page.bth_elements.click()
    element_page_text = page.elements_text.get_text()
    assert element_page_text == 'Please select an item from left to start practice.'


def test_page_elemants(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'

    assert elements_page.icon.exist()
    assert elements_page.bth_sidebar_first.exist()
    assert elements_page.bth_sidebar_first_textbox.exist()




