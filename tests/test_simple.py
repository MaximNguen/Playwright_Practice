from playwright.sync_api import Page, expect
import pytest

from pages.simple_page import SimplePage

class TestSimplePage:
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.simple_page = SimplePage(page)
        
    def test_simple_exists(self):
        self.simple_page.open()
        self.simple_page.check_element_visible("input[name='submit']")
        
    def test_simple_click(self):
        self.simple_page.open()
        self.simple_page.click_button("input[name='submit']")
        self.simple_page.expect_text("p#result-text", "Submitted")