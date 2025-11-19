from playwright.sync_api import Page, TimeoutError, expect
import random
from datetime import datetime
import time
import pytest

class Events:

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

    def open(self, baseURL, port):
        self.page.goto(f'{baseURL}:{port}/events')

    def open_create_event(self):
        self.page.locator('xpath=//*[contains(text(), "Добавить мероприятие")]/parent::*').click()
        self.page.wait_for_function(
            """() => {
                const elem = document.evaluate('//body', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                if (!elem) return false;
                const classValue = elem.getAttribute('class') || '';
                return classValue.includes('ant-scrolling-effect');
            }""",
            timeout=5000
        )
        time.sleep(0.5)

    def fill_everything_nessesary(self):
        try:
            number = random.randint(100, 999)
            now = datetime.now()
            date = now.strftime('.%m.%Y')
            month = int(now.strftime('%m'))
            year = int(now.strftime('%Y'))
            startday = int(now.strftime('%d'))
            endday = int(startday + 2)
            if month in [2] and endday >= 28:
                endday = endday - 28
                month = month + 1
            elif month in [4, 6, 9, 11] and endday >= 30:
                endday = endday - 30
                month = month + 1
            elif endday >= 31:
                endday = endday - 31
                month = month + 1
            enddate = f'.{month}.{year}'
            main_jud = 'Зариковская Наталья Вячеславовна'
            main_sec = 'Жуков Илья Романович'
            print(endday, date)
            name_input = self.page.locator('xpath=//p[contains(text(), "Название мероприятия")]/following-sibling::input')
            expect(name_input).to_be_editable(timeout=10000)
            name_input.fill(f'Аэробика-{number}')
            status_input = self.page.locator('xpath=//p[contains(text(), "Статус мероприятия")]/following::input')
            expect(status_input).to_be_clickable(timeout=10000)
            status_input.click()
            vs_option = self.page.locator('xpath=//div[contains(text(), "Всероссийские")]')
            expect(vs_option).to_be_clickable(timeout=10000)
            vs_option.click()
            subject_input = self.page.locator('xpath=//p[contains(text(), "Субъект")]/following::input')
            expect(subject_input).to_be_clickable(timeout=10000)
            subject_input.click()
            tomsk_option = self.page.locator('xpath=//div[@title="Томская область"]')
            expect(tomsk_option).to_be_clickable(timeout=10000)
            tomsk_option.click()
            city_input = self.page.locator('xpath=//p[contains(text(), "Город")]/following::input')
            expect(city_input).to_be_clickable(timeout=10000)
            city_input.click()
            tomsk_city_option = self.page.locator('xpath=//div[@title="г. Томск"]')
            expect(tomsk_city_option).to_be_clickable(timeout=10000)
            tomsk_city_option.click()
            address_input = self.page.locator('xpath=//p[contains(text(), "Адрес")]/following-sibling::input')
            expect(address_input).to_be_editable(timeout=10000)
            address_input.fill(f'Адрес-{number}')
            sport_complex_input = self.page.locator('xpath=//p[contains(text(), "Спорткомплекс")]/following-sibling::input')
            expect(sport_complex_input).to_be_editable(timeout=10000)
            sport_complex_input.fill(f'СК-{number}')
            start_date_input = self.page.locator('xpath=//p[contains(text(), "Дата начала соревнования")]/following::input')
            expect(start_date_input).to_be_editable(timeout=10000)
            start_date_input.fill(f'{startday}{date}')
            end_date_input = self.page.locator('xpath=//p[contains(text(), "Дата окончания соревнования")]/following::input')
            expect(end_date_input).to_be_editable(timeout=10000)
            end_date_input.fill(f'{endday}{enddate}')
            app_start_input = self.page.locator('xpath=//p[contains(text(), "Дата начала приема заявок")]/following::input')
            expect(app_start_input).to_be_editable(timeout=10000)
            app_start_input.fill(f'{startday}{date}')
            app_end_input = self.page.locator('xpath=//p[contains(text(), "Дата окончания приема заявок")]/following::input')
            expect(app_end_input).to_be_editable(timeout=10000)
            app_end_input.fill(f'{startday}{date}')
            expect(name_input).to_be_clickable(timeout=10000)
            name_input.click()
            age_groups = self.page.locator('xpath=//div[@name="ageGroups"]')
            expect(age_groups).to_be_clickable(timeout=10000)
            age_groups.click()
            age_12_14 = self.page.locator('xpath=//div[@title="12-14 лет"]')
            expect(age_12_14).to_be_clickable(timeout=10000)
            age_12_14.click()
            age_15_17 = self.page.locator('xpath=//div[@title="15-17 лет"]')
            expect(age_15_17).to_be_clickable(timeout=10000)
            age_15_17.click()
            age_18_plus = self.page.locator('xpath=//div[@title="18 и старше"]')
            expect(age_18_plus).to_be_clickable(timeout=10000)
            age_18_plus.click()
            expect(name_input).to_be_clickable(timeout=10000)
            name_input.click()
            nominations = self.page.locator('xpath=//div[@name="nominations"]')
            expect(nominations).to_be_clickable(timeout=10000)
            nominations.click()
            select_all = self.page.locator('xpath=//div[@title="Трио"]/preceding-sibling::div[@title="Выбрать все"]')
            expect(select_all).to_be_clickable(timeout=10000)
            select_all.click()
            expect(name_input).to_be_clickable(timeout=10000)
            name_input.click()
            main_judge_input = self.page.locator('xpath=//p[contains(text(), "Главный судья")]/following::input')
            expect(main_judge_input).to_be_editable(timeout=10000)
            main_judge_input.fill(main_jud)
            main_judge_option = self.page.locator(f'xpath=//div[@title="{main_jud}"]')
            expect(main_judge_option).to_be_clickable(timeout=10000)
            main_judge_option.click()
            main_sec_input = self.page.locator('xpath=//p[contains(text(), "Главный секретарь")]/following::input')
            expect(main_sec_input).to_be_editable(timeout=10000)
            main_sec_input.fill(main_sec)
            main_sec_option = self.page.locator(f'xpath=//div[@title="{main_sec}"]')
            expect(main_sec_option).to_be_clickable(timeout=10000)
            main_sec_option.click()
        except Exception as e:
            if "stale" in str(e).lower():
                pytest.fail('StaleElementReferenceException: Что-то пошло не так при создании мероприятия. Попробуйте запустить снова')
            else:
                raise

    def save_event(self):
        save_button = self.page.locator('xpath=//button[@type="button" and contains(text(), "Сохранить")]')
        expect(save_button).to_be_clickable(timeout=10000)
        save_button.click()
        self.page.wait_for_selector('xpath=//div[@class="ant-modal-wrap"]', state='detached', timeout=3000)