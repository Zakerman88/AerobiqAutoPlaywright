from playwright.sync_api import Page, TimeoutError, expect
from pages.aerobiq_dnd import DragAndDrop
import time
import pytest

class Brigades:

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
        self.page.goto(f'{URL}/brigades')

    def open_edit_brigades(self):
        current_url = self.page.url
        self.page.locator('xpath=//*[contains(text(), "Сформировать судейские бригады")]/parent::*').click()
        self.page.wait_for_url(lambda url: url != current_url, timeout=10000)

    def create_brigades(self, count):
        try:
            dnd = DragAndDrop(self.page)
            list_counted_pages = self.page.query_selector_all('xpath=//div[@class="ant-tabs-tab"]')
            len_of_list_counted_pages = len(list_counted_pages) + 1
            j = 1
            while j < len_of_list_counted_pages:
                execution_judge_count = self.page.locator('xpath=//div[@tabindex="0"]/following::*[@name="executionJudgeCount"]')
                expect(execution_judge_count).to_be_clickable(timeout=10000)
                execution_judge_count.click()
                count_option = self.page.locator(f'xpath=//div[@class="rc-virtual-list-holder-inner"]/child::div[@title="{count}"]')
                expect(count_option).to_be_clickable(timeout=10000)
                count_option.click()
                i = 0
                dnd_xpath_locator = '//div[@class=""]/descendant::*[@style="cursor: grab;"]'
                dnd_attribute_ = 'area-pressed'
                dnd_text_ = 'true'
                while True:
                    try:
                        drop = self.page.locator('xpath=//div[contains(text(), "Судья линии")]/following::*[@class="ant-card-body"]/child::*')
                        expect(drop).to_be_clickable(timeout=10000)
                        time.sleep(0.2)
                        drop.scroll_into_view_if_needed()
                        time.sleep(0.3)
                        drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                        expect(drag).to_be_clickable(timeout=10000)
                        dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                        drop = self.page.locator(f'xpath=//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Председатель")]/following::*[@class="ant-card-body"]/child::div')
                        expect(drop).to_be_clickable(timeout=10000)
                        time.sleep(0.2)
                        drop.scroll_into_view_if_needed()
                        time.sleep(0.3)
                        drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                        expect(drag).to_be_clickable(timeout=10000)
                        dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                        k = 0
                        while k != count:
                            drops = self.page.query_selector_all(f'xpath=//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Судьи исполнения")]/following::*[@class="ant-card-body"]/child::*')
                            drop = drops[i] if i < len(drops) else None
                            if drop:
                                time.sleep(0.2)
                                drop.scroll_into_view_if_needed()
                                time.sleep(0.3)
                                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                                expect(drag).to_be_clickable(timeout=10000)
                                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                            drops = self.page.query_selector_all(f'xpath=//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Судья артистичности")]/following::*[@class="ant-card-body"]/child::*')
                            drop = drops[i] if i < len(drops) else None
                            if drop:
                                time.sleep(0.2)
                                drop.scroll_into_view_if_needed()
                                time.sleep(0.3)
                                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                                expect(drag).to_be_clickable(timeout=10000)
                                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
                            k = k + 1

                        k = 0
                        while k != 2:
                            drops = self.page.query_selector_all(f'xpath=//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Судьи сложности")]/following::*[@class="ant-card-body"]/child::*')
                            drop = drops[i] if i < len(drops) else None
                            if drop:
                                time.sleep(0.2)
                                drop.scroll_into_view_if_needed()
                                time.sleep(0.3)
                                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                                expect(drag).to_be_clickable(timeout=10000)
                                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
                            k = k + 1

                        i = i + 1
                        if i == 2:
                            break
                    except TimeoutError:
                        print("Распределение судей окончено")
                        break

                drop = self.page.locator('xpath=//div[contains(text(), "Судья секундометрист")]/following::*[@class="ant-card-body"]/child::*')
                expect(drop).to_be_clickable(timeout=10000)
                time.sleep(0.2)
                drop.scroll_into_view_if_needed()
                time.sleep(0.3)
                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                expect(drag).to_be_clickable(timeout=10000)
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                drop = self.page.locator('xpath=//div[contains(text(), "Судья информатор")]/following::*[@class="ant-card-body"]/child::*')
                expect(drop).to_be_clickable(timeout=10000)
                time.sleep(0.2)
                drop.scroll_into_view_if_needed()
                time.sleep(0.3)
                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                expect(drag).to_be_clickable(timeout=10000)
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                drop = self.page.locator('xpath=//div[contains(text(), "Судья при участниках")]/following::*[@class="ant-card-body"]/child::*')
                expect(drop).to_be_clickable(timeout=10000)
                time.sleep(0.2)
                drop.scroll_into_view_if_needed()
                time.sleep(0.3)
                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                expect(drag).to_be_clickable(timeout=10000)
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                drop = self.page.locator('xpath=//div[contains(text(), "Технический секретарь")]/following::*[@class="ant-card-body"]/child::*')
                expect(drop).to_be_clickable(timeout=10000)
                time.sleep(0.2)
                drop.scroll_into_view_if_needed()
                time.sleep(0.3)
                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                expect(drag).to_be_clickable(timeout=10000)
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                drop = self.page.locator('xpath=//div[contains(text(), "Судья по музыке")]/following::*[@class="ant-card-body"]/child::*')
                expect(drop).to_be_clickable(timeout=10000)
                time.sleep(0.2)
                drop.scroll_into_view_if_needed()
                time.sleep(0.3)
                drag = self.page.locator('xpath=//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                expect(drag).to_be_clickable(timeout=10000)
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                next_page_button = self.page.query_selector_all('xpath=//div[@class="ant-tabs-tab"]')
                time.sleep(0.2)
                if next_page_button:
                    next_page_button[0].scroll_into_view_if_needed()
                    current_url = self.page.url
                    if j == 1:
                        next_page_button[0].click()
                    else:
                        next_page_button[1].click() if len(next_page_button) > 1 else None
                    self.page.wait_for_url(lambda url: url != current_url, timeout=10000)
                j = j + 1
        except Exception as e:
            if "target out of bounds" in str(e).lower():
                pytest.fail('MoveTargetOutOfBounds: Плохо прицелился')
            else:
                raise