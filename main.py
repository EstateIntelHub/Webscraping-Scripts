import time

from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context with a custom user agent
    generic_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    context = browser.new_context(user_agent=generic_user_agent)

    # Use the new context to open a new page
    page = context.new_page()

    page.goto("https://www.imobiliare.ro/inchirieri-individuale/timisoara/elisabetin/casa-individuala-de-inchiriat-3-camere-XC881113A")

    # Select the div element by its ID
    specific_div = page.query_selector('#b_detalii_specificatii')

    # Get the HTML content of the div
    if specific_div:
        html_content = specific_div.inner_html()

        # Write the HTML content to a file
        with open('div_content.html', 'w', encoding='utf-8') as file:
            file.write(html_content)
    else:
        print("Div with specified ID not found")

    # Note: Browser is not closed here, it will stay open after the script finishes


    time.sleep(100)

with sync_playwright() as playwright:
    run(playwright)
