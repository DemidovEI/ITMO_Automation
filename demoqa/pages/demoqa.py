
from pages.base_page import BasePage
from components.components import WebElement


class Demoqa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.bth_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, '#app > footer > span')
        self.elements_text = WebElement(driver, '#app > div > div > div.row > div:nth-child(2)')










