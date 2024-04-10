from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = browser.new_page()
    page.goto("https://www.imoradar24.ro/case-de-inchiriat/timisoara")

    # Extracting titles of listings
    listings = page.query_selector_all(".mb-4")  # Use the appropriate selector

    with open('listings.txt', 'w', encoding='utf-8') as file:  # Open a file for writing
        for listing in listings:
            title = listing.text_content().strip()  # Get the text content
            print(title)  # Print the title
            file.write(title + '\n')  # Write the title to the file

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
