from playwright.sync_api import Page, TimeoutError, expect
from pages.aerobiq_dnd import DragAndDrop
import pytest

class Program:

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
        self.page.goto(f'{URL}/program/edit')

    def open_start_program(self, URL):
        self.page.goto(f'{URL}/')

    def start_program(self):
        start_button = self.page.locator('xpath=/html/body/div[1]/div/main/div[2]/div/div/button')
        expect(start_button).to_be_clickable(timeout=10000)
        start_button.click()
        self.page.wait_for_function(
            """() => {
                const elem = document.evaluate('//div[@class="ant-modal-wrap"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                if (!elem) return false;
                const style = elem.getAttribute('style') || '';
                return !style.includes('display: none');
            }""",
            timeout=5000
        )
        self.page.locator('xpath=/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button').click()

    def open_edit_event_program(self):
        current_url = self.page.url
        self.page.locator('xpath=//*[contains(text(), "Редактировать")]/parent::*').click()
        self.page.wait_for_url(lambda url: url != current_url, timeout=10000)
        checkboxes = self.page.locator('xpath=//*[@type="checkbox"]').all()
        for checkbox in checkboxes[1:]:
            checkbox.click()

    def set_event_program(self):
        dnd = DragAndDrop(self.page)
        list_dnd = self.page.query_selector_all('xpath=//div[@class="sc-GKYbw eWVKHj"]/descendant::*[@style="cursor: grab;"]')
        len_of_list_dnd = len(list_dnd)
        print('Номинаций всего: ', len_of_list_dnd)
        i = 0
        dnd_xpath_locator = '//div[@class="sc-GKYbw eWVKHj"]/child::*'
        dnd_attribute_ = 'style'
        dnd_text_ = 'transition: transform linear;'
        while True:
            drag = self.page.locator('xpath=//div[@class="sc-GKYbw eWVKHj"]/child::*')
            expect(drag).to_be_clickable(timeout=10000)
            drop = self.page.locator('xpath=//span[contains(text(), "1 бригада")]/following::*[@class="sc-UpCWa gwtxli"]')
            expect(drop).to_be_clickable(timeout=10000)
            dnd.dragndrop_program(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
            i = i + 1
            if i == len_of_list_dnd:
                print('Номинаций готово: ', i)
                break

            drag = self.page.locator('xpath=//div[@class="sc-GKYbw eWVKHj"]/child::*')
            expect(drag).to_be_clickable(timeout=10000)
            drop = self.page.locator('xpath=//span[contains(text(), "2 бригада")]/following::*[@class="sc-UpCWa gwtxli"]')
            expect(drop).to_be_clickable(timeout=10000)
            dnd.dragndrop_program(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
            i = i + 1