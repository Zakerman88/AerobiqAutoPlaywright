from playwright.sync_api import Page, Locator, TimeoutError, expect
import time
import pytest

class Applications:

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
        self.page.goto(f'{URL}/applications')

    def open_create_application_window(self):
        create_button = self.page.locator('xpath=/html/body/div[1]/div/main/div[2]/div/div[1]/div/div[3]/button')
        expect(create_button).to_be_clickable(timeout=10000)
        create_button.click()

    def choose_trainer(self, name):  # name - фамилия имя
        while True:
            try:
                open_trainers = self.page.locator('xpath=//*[@id="rc_select_0"]')
                open_trainers.click()
                find_trainer = self.page.locator(f'xpath=//div[@class="ant-select-item-option-content" and contains(text(), "{name}")]')
                expect(find_trainer).to_be_clickable(timeout=2000)
                if find_trainer.is_visible():
                    find_trainer.click()
                    break
            except TimeoutError:
                print('Тренер не найден, продолжается поиск')
                list_locator = self.page.locator('xpath=//*[@class="rc-virtual-list"]')
                expect(list_locator).to_be_visible(timeout=2000)
                list_locator.press('ArrowDown')

    def choose_organisation(self):  # берёт первую попавшуюся организацию
        choose_organisation = self.page.locator('xpath=/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/span[2]')
        expect(choose_organisation).to_be_clickable(timeout=10000)
        choose_organisation.click()
        find_organisation = self.page.locator('xpath=/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]')
        find_organisation.click()

    # def choose_exact_organisation(self, name): # берёт какую напишут
    #     open_organisations = self.page.locator('xpath=//*[@id="rc_select_1"]')
    #     open_organisations.click()
    #     find_organisation = self.page.locator(f'partial link={name}')
    #     find_organisation.click()

    def save_application(self):
        create_button = self.page.locator('xpath=/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button')
        current_url = self.page.url
        create_button.click()
        self.page.wait_for_url(lambda url: url != current_url, timeout=10000)

    def open_add_nomination_window(self):
        add_button = self.page.locator('xpath=/html/body/div[1]/div/main/div[2]/div/div[2]/button')
        add_button.click()

    def choose_age(self, age):  # 12(1)/15(2)/18(3)
        open_ages = self.page.locator('xpath=//*[@id="rc_select_2"]')
        open_ages.click()
        find_age = self.page.locator(f'xpath=/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[{age}]')
        find_age.click()

    def choose_disc(self, disc):  # 1/2/3/4/5/6/7
        open_discs = self.page.locator('xpath=//*[@id="rc_select_3"]')
        open_discs.click()
        find_disc = self.page.locator(f'xpath=/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[{disc}]/div')
        open_discs.click()  # Note: This seems like a potential typo in original; keeping as is
        find_disc.click()

    def save_nomination(self):
        save_button = self.page.locator('xpath=/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button')
        save_button.click()
        self.page.wait_for_function(
            """() => {
                const elem = document.evaluate('//div[@class="ant-modal-wrap"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                return elem && elem.style.display === 'none';
            }""",
            timeout=5000
        )

    def open_add_sports_window(self):
        add_button = self.page.locator('xpath=/html/body/div[1]/div/main/div[2]/div/div[3]/div/section/div/div[2]/div[1]/span')
        expect(add_button).to_be_clickable(timeout=10000)
        add_button.click()

    def add_1_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[8]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=2000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_2_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[9]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=3000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_3_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=3000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_4_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[11]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=3000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_5_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[12]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=3000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_6_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[7]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[13]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=3000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_7_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[8]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[14]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=3000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_8_sportik(self):
        open_sportik = self.page.locator('xpath=/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[9]/div/div')
        expect(open_sportik).to_be_clickable(timeout=10000)
        open_sportik.click()
        try:
            choose_sportik = self.page.locator('xpath=/html/body/div[15]/div/div/div/div[2]/div[1]/div/div/div[1]')
            expect(choose_sportik).to_be_clickable(timeout=3000)
            choose_sportik.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def add_next_sports(self):
        try:
            next_sports_button = self.page.locator('css=.sc-iveFHk > .jewgFb')
            expect(next_sports_button).to_be_clickable(timeout=10000)
            next_sports_button.click()
        except TimeoutError:
            element = self.page.locator('xpath=//div[@class="ant-empty-description"]')
            print(f'{element.inner_text()}')
            text_to_check = 'Нет данных'
            if text_to_check == element.inner_text():
                pytest.xfail('Недостаточно спортсменов для нового выступления')
            else:
                pytest.fail('TimeoutError: Неизвестная ошибка при добавлении спортсмена')

    def send_applications(self):
        check_pages = self.page.locator('xpath=//a[@rel="nofollow"]')
        expect(check_pages).to_be_clickable(timeout=1000)
        list_counted_pages = self.page.query_selector_all('xpath=//a[@rel="nofollow"]')
        len_of_list_counted_pages = len(list_counted_pages)
        for j in range(len_of_list_counted_pages):
            page_button = self.page.locator(f'xpath=//a[@rel="nofollow" and contains(text(), "{j+1}")]')
            expect(page_button).to_be_clickable(timeout=5000)
            page_button.click()
            time.sleep(0.3)
            list_created_applications = self.page.query_selector_all('xpath=//*[@class="ant-space-item" and contains(text(), "Черновик")]/following::span[@class="anticon anticon-edit"]')
            len_of_list_created_applications = len(list_created_applications)
            for i in range(len_of_list_created_applications):
                time.sleep(0.3)
                try:
                    edit_button = self.page.locator('xpath=//*[@class="ant-space-item" and contains(text(), "Черновик")]/following::span[@class="anticon anticon-edit"]')
                    expect(edit_button).to_be_clickable(timeout=2000)
                    edit_button.click()
                except TimeoutError:
                    print("Черновики не найдены")
                time.sleep(0.2)
                try:
                    accept_button = self.page.locator('xpath=//button[@type="button" and contains(text(), "Подтвердить")]')
                    expect(accept_button).to_be_clickable(timeout=2000)
                    accept_button.click()
                except TimeoutError:
                    print("Кнопка 'Подтвердить' не найдена")

    def accept_applications(self):
        check_pages = self.page.locator('xpath=//a[@rel="nofollow"]')
        expect(check_pages).to_be_clickable(timeout=2000)
        list_counted_pages = self.page.query_selector_all('xpath=//a[@rel="nofollow"]')
        len_of_list_counted_pages = len(list_counted_pages)
        for j in range(len_of_list_counted_pages):
            page_button = self.page.locator(f'xpath=//a[@rel="nofollow" and contains(text(), "{j+1}")]')
            expect(page_button).to_be_clickable(timeout=5000)
            page_button.click()
            time.sleep(0.3)
            list_created_applications = self.page.query_selector_all('xpath=//*[@class="ant-space-item" and contains(text(), "На рассмотрении")]/following::span[@class="anticon anticon-edit"]')
            len_of_list_created_applications = len(list_created_applications)
            for i in range(len_of_list_created_applications):
                time.sleep(0.3)
                try:
                    edit_button = self.page.locator('xpath=//*[@class="ant-space-item" and contains(text(), "На рассмотрении")]/following::span[@class="anticon anticon-edit"]')
                    expect(edit_button).to_be_clickable(timeout=2000)
                    edit_button.click()
                except TimeoutError:
                    print("На рассмотрении не найдены")
                time.sleep(0.2)
                try:
                    accept_button = self.page.locator('xpath=//button[@type="button" and contains(text(), "Подтвердить")]')
                    expect(accept_button).to_be_clickable(timeout=2000)
                    accept_button.click()
                except TimeoutError:
                    print("Кнопка 'Подтвердить' не найдена")