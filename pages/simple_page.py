from playwright.sync_api import Page, expect

from conftest import page

class SimplePage:
    def __init__(self, page: Page):
        self.page = page
        
    def open(self):
        self.page.goto("https://www.qa-practice.com/elements/button/simple")
        
    def get_element(self, locator: str):
        self.check_element_visible(locator)
        return self.page.locator(locator)
    
    def check_element_visible(self, locator: str):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible()
    
    def click_button(self, locator: str):
        button = self.page.locator(locator)
        button.click()
        
    def expect_text(self, locator: str, expected_text: str):
        text_element = self.page.locator(locator)
        expect(text_element).to_have_text(expected_text)