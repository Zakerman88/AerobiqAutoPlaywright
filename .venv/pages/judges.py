from playwright.sync_api import Page, TimeoutError, expect
import pytest

class Judges:

    def __init__(self, page: Page):
        self.page = page

    def authorization(self, username, password, baseURL, port):
        URL = f'{baseURL}:{port}'
        self.page.goto(URL)
        while True:
            try:
                self.page.fill('input[name="login"]', username)
                self.page.fill('input[name="password"]', password)
                current_url = self.page.url
                self.page.click('xpath=/html/body/div[1]/div/div/div[1]/div/form/button')
                self.page.wait_for_url(lambda url: url != current_url, timeout=10000)
            except TimeoutError:
                pytest.fail('TimeoutError: Страница недоступна (timeout 10sec)')
            else:
                break

    def open(self, URL):
        self.page.goto(f'{URL}/judges')

    def add_judges(self):
        add_button = self.page.locator('xpath=/html/body/div[1]/div/main/div[2]/div/div[1]/button')
        expect(add_button).to_be_clickable(timeout=10000)
        add_button.click()
        self.page.wait_for_function(
            """() => {
                const elem = document.evaluate('//div[@class="ant-modal-wrap"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                if (!elem) return false;
                const style = elem.getAttribute('style') || '';
                return !style.includes('display: none');
            }""",
            timeout=5000
        )
        self.page.locator('xpath=//*[@id="rc_select_0"]').click()
        self.page.locator('xpath=/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[1]').click()
        list_of_checkboxes = self.page.query_selector_all('xpath=//span[@class="ant-checkbox"]')
        for checkbox in list_of_checkboxes:
            checkbox.click()
        self.page.locator('xpath=/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button').click()
        self.page.wait_for_function(
            """() => {
                const elem = document.evaluate('//div[@class="ant-modal-wrap"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                return elem && elem.style.display === 'none';
            }""",
            timeout=5000
        )