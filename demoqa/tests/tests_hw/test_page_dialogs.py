from pages.modal_dialogs import ModalDialog
from pages.demoqa import Demoqa


def test_modal_elements(browser):
    modal_dialog_page = ModalDialog(browser)

    modal_dialog_page.visit()
    assert modal_dialog_page.btns_menu.check_count_elements(count=5)


def test_navigation_modal(browser):
    modal_dialog_page = ModalDialog(browser)
    demo_qa_page = Demoqa(browser)

    modal_dialog_page.visit()
    modal_dialog_page.refresh()
    browser.refresh()
    modal_dialog_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)



