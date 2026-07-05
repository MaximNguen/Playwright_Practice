import pytest
from playwright.sync_api import Page

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.close()