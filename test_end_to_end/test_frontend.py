import re
import pytest

from playwright.sync_api import Page, expect



API_URL = "http://localhost:8501/" 

def test_homepage(page: Page):
    page.goto(API_URL)

   
    expect(page).to_have_title(re.compile("overview"))

    data_collection = page.get_by_role("link", name="data_collection")
    data_update = page.get_by_role("link", name="data_update")

    page.screenshot(path="screenshot.png", full_page=True)

    
def test_page_data_collection(page: Page):
    
    page.goto(API_URL + "data_collection")

    expect(page).to_have_title(re.compile("data_collection"))

    
    page.get_by_role("textbox", name="name").fill("MariaSmith")

    page.get_by_role("button", name="Submit").click()

    page.screenshot(path="screenshot_new.png", full_page=True)
    

    
def test_page_data_update(page: Page):
    
    page.goto(API_URL + "data_update")

    expect(page).to_have_title(re.compile("data_update"))

    
    page.get_by_role("textbox", name="What do you want to change?").fill("raport101")

    page.get_by_role("button", name="Submit").click()

    page.screenshot(path="screenshot_new.png", full_page=True)