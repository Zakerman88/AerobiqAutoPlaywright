from pages.events import Events
from playwright.sync_api import TimeoutError
import pytest

username = 'admin@admin.com'
password = 'SomeSecure^17$58'
baseURL = 'https://juds-client-admin-stage.aldera-soft.ru'
port = '8084'

def test_create_new_event(page):
    i = 1
    ev = Events(page)
    ev.authorization(username, password, baseURL, port)
    while True:
        try:
            print(f'Попытка №{i}')
            ev.open(baseURL, port)
            ev.open_create_event()
            ev.fill_everything_nessesary()
            ev.save_event()
        except TimeoutError:
            if i == 3:
                pytest.fail("TimeoutError 3 times in a row: Не все обязательные поля заполнены/Введены невалидные данные")
            i = i + 1
        else:
            break