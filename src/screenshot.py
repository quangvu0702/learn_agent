from playwright.async_api import async_playwright
import asyncio

async def take_screenshot(input_fn, output_fn):
    """
    Take a screenshot of the HTML file and save it as a PNG file.
    """
    html_content = open(input_fn, "r").read()
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        await page.screenshot(path=output_fn)
        await browser.close()
        print(f"Screenshot saved as '{output_fn}'")

# Example usage
if __name__ == "__main__":
    input_file = "data/sample.html"
    output_file = "data/output_image.png"
    asyncio.run(take_screenshot(input_file, output_file)) 