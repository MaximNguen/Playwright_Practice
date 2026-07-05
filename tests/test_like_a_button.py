from playwright.sync_api import Page, expect

def test_like_a_button_exists(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like-a-button")
    button = page.locator(".a-button")
    expect(button).to_be_visible()
    
def test_like_a_button_click(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like-a-button")
    button = page.locator(".a-button")
    button.click()
    expected_text = page.locator("#result-text")
    expect(expected_text).to_have_text("Submitted")