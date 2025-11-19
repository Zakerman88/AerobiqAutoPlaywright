from pages.applications import Applications
from pages.event_program import Program
from pages.judges import Judges
from pages.brigades import Brigades
from pages.events import Events
import time
import pytest

username = 'admin@admin.com'
password = 'SomeSecure^17$58'
###
baseURL = 'https://juds-client-admin-stage.aldera-soft.ru'
port = '8084'
category = 'events'
eventID = 'f8b80940-e91a-40e1-ad34-6cd3965daef6'
URL = f'{baseURL}:{port}/{category}/{eventID}'
###
dayCount = 3 # 1 или 3, количество дней в мероприятии
###
IndWomanTrainers = ['Борисова', 'Зверева', 'Хасикян', 'Гусева', 'Хандов']
IndManTrainers = ['Хандов', 'Гусева', 'Борисова', 'Зверева']
TrioTrainers = ['Хоружева', 'Хандов']
GPTrainers = ['Хандов', 'Зверева']
TGTrainers = ['Хандов', 'Пашкова']
###
small = 1
middle = 2
high = 3
# в зависимости от выбранных на соревнования возрастных групп (при 10-12, 15-17, 18+ - 1=10-12, 2=15-17, 3=18+)
###
IndWoman = 1
IndMan = 2
Trio = 3
Gruppa = 4
TG = 5
GP = 6
SmeshPara = 7
# номинации 1=ИЖ, 2=ИМ, 3=трио, 4=группа-5, 5=ТГ, 6=ГП, 7=смеш.пара

@pytest.mark.quick
def test_add_IndWoman1(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[0]) #выбор тренера
    time.sleep(2)
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1) #задержка без которой поля для клика перерываются уведомлениями об успешном добавлении

def test_add_IndWoman2(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman3(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[2]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman4(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[3]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman5(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[4]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman6(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[4]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman7(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[4]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan1(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan2(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan3(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[2]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan4(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[3]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_Trio1(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TrioTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(Trio) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_Trio2(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TrioTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(Trio) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_TG1(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TGTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(TG) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_4_sportik()
        app.add_5_sportik()
        app.add_6_sportik()
        app.add_7_sportik()
        app.add_8_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_TG2(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TGTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(TG) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_4_sportik()
        app.add_5_sportik()
        app.add_6_sportik()
        app.add_7_sportik()
        app.add_8_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_GP1(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(GPTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(GP) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_4_sportik()
        app.add_5_sportik()
        app.add_6_sportik()
        app.add_7_sportik()
        app.add_8_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_GP2(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(GPTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(GP) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while True: #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_4_sportik()
        app.add_5_sportik()
        app.add_6_sportik()
        app.add_7_sportik()
        app.add_8_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_accept_all_applications(page):
    app = Applications(page)
    app.authorization(username, password, baseURL, port) #авторизация
    app.open(URL)
    app.send_applications()
    app.accept_applications()

@pytest.mark.start
def test_start_program(page):
    prog = Program(page)
    prog.authorization(username, password, baseURL, port)
    prog.open_start_program(URL)
    prog.start_program()

@pytest.mark.start
def test_add_judges(page):
    jud = Judges(page)
    jud.authorization(username, password, baseURL, port)
    jud.open(URL)
    i=0
    while i != 29:
        jud.add_judges()
        i = i + 1

@pytest.mark.start
def test_judges_teams(page):
    br = Brigades(page)
    br.authorization(username, password, baseURL, port)
    br.open(URL)
    br.open_edit_brigades()
    br.create_brigades(4)

@pytest.mark.start
def test_set_program_plan(page):
    prog = Program(page)
    prog.authorization(username, password, baseURL, port)
    prog.open(URL)
    prog.set_event_program()