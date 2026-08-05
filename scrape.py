# scrape.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://aadityaks.is-a.dev/", timeout=30000)
    print(page.title())
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(page.content())
    browser.close()