import re
import datetime as dt
#структура таблиц
titles = {'bus.txt':('ID автобуса', 'Госномер', 'Марка', 'Статус','ID водителя', 'ID маршрута'),\
    'driver.txt': ('ID водителя', 'Фамилия', 'Имя', 'Отчество','Дата рождения', 'Стаж', 'Телефон'),\
    'routes.txt': ('ID маршрута', 'Номер маршрута', 'Маршрут')}

'''Функции отвечающие за печать'''

#Печать данных из файла
def print_data(file):
    global titles
    with open(file, 'r', encoding='UTF-8') as f:
        data = (i.rstrip().split(',') for i in f)
        temp = {j[0]:j[1:] for j in data}
        for item in titles[file]: 
            print(item.center(14), end='')
        print()
        for k, v in temp.items():
            print(k.center(14), end='')
            [print(i.center(14), end='') for i in v]
            print()

#функции печати из заданных файлов
def print_bus():
    print_data('bus.txt')
def print_drivers():
    print_data('driver.txt')
def print_routes():
    print_data('routes.txt')

'''Функции для корректного ввода данных'''
#функция для ввода корректного номера ТС
def correctBusNumber():
    pattern = r'[ABCEHKMOPTXY|АВСЕНКМОРТХУ]\d{3}[ABCEHKMOPTXY|АВСЕНКМОРТХУ]{2}\d{2,3}'
    while True:
        print('Введите государственный номер ТС в формате X111XX12 или X111XX123: ')
        number = input().upper()
        if re.fullmatch(pattern, number):              
            return number
            
        else: print('Введен не корректный государственный номер')

#функция для выбора корректного статуса ТС
def correctStatus():
    while True:
        print('''Нажмите 1, если хотите выбрать статус "Исправен"
Нажмите 2, если хотите выбрать статус "Ремонт"''')
        num = input()
        if num == '1': return "Исправен"
        elif num == '2': return "Ремонт"
        else: print("Некорректный ввод, повторите еще раз")

#функция для выбора id 
def chooseID(file):
    with open(file, 'r', encoding='UTF-8') as f:
        print_data(file)
    while True:
        with open(file, 'r', encoding='UTF-8') as f:
            print('Выберите идентификатор маршрута')

            id = input(">>> ")
            if id in [i.split(',')[0] for i in f]:
                return id
            else: print("введен некорректный ID. Поробуйте еще раз")

#функция для выбора id водителя
def chooseDriver():
    return chooseID('driver.txt')

#функция для выбора id маршрута
def chooseRoute():
    return chooseID('routes.txt')

#функция для выбора id автобуса
def chooseBus():
    return chooseID('bus.txt')

#ввод ФИО
def correctName(text):
    while True:
        name = input(f'Введите {text} водителя >>> ').rstrip()
        if name.isalpha():
            return name.capitalize()
        print('Введено некорректное имя')


#ввод корректного номера телефона
def correctPhoneNumber():
    while True:
        pattern = r'\b\+?[7,8]?(\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b'
        try:
            num = input("Введите номер телефона >>> ")
            number = re.findall(pattern, num)
            if number[0]:
                return f'8({number[0][-10:-7]}){number[0][-7:-4]}-{number[0][-4:-2]}-{number[0][-2:]}'
            else: raise Exception
        except: print('Номер введен некорректно, попробуйте еще раз')

#ввод корректной даты 
def correctDate(text, result='date'):
    while True:
        try:
            num = input(f"Введите дату {text} в формате 'DD.MM.YYYY' >>> ")
            date_format = "%d.%m.%Y"
            d2 = dt.datetime.today()
            d1 = dt.datetime.strptime(num, date_format)
            delta = d2 - d1
            old = delta.days // 365
            if result == 'date':
                if 17 < old < 70:
                    return (d1.date().strftime(date_format), old)
            elif result == 'years':
                return (d1.date().strftime(date_format), old)
            else: raise Exception
        except: print('Данные введены некорректно, попробуйте еще раз')

#ввод корректной даты рождения
def birthDate():
    return correctDate('рождения')

#определение стажа
def timeWorkStart():
    return correctDate('начала работы водителем', result='years')

#ввод маршрута
def enterRoute():
    count = 0
    def string(text): return text.replace(' ', '').isalnum()
    res = ''
    while True:
        if not count:
            temp = input("Введите название начальной точки маршрута> ")
            if string(temp):
                res += temp.capitalize()
                count+=1
            continue
        elif count==1:
            print("Введите название следующей точки маршрута> ")
            temp = input()
            if string(temp):
                res += ' - ' + temp.capitalize()
                count+=1
            continue
        else: 
            print("Введите название следующей точки маршрута или нажмите Enter чтобы завершить ввод> ")
            temp = input()
            if string(temp):
                res += ' - ' + temp.capitalize()
                count+=1
                continue
            else:
                return res

#ввод корректного номера маршрута с проверкой уникальности
def enterRouteNumber():
    with open('routes.txt', 'r', encoding='UTF-8') as f:
        routes = [i.split(',')[1] for i in f.readlines()]
    while True:
        try:
            print("Введите номер маршрута>>> ")
            num = str(int(input()))
            if not num in routes:
                return num
            else: raise Exception
        except ValueError: print('Введено нечисловое значение!')
        except: print('такой номер маршрута уже существует!')

'''Функции для добавления информации в файлы .txt'''

#добавление в файл общая функция
def add_info(file, func, *args):
    while True:
            print("Проверьте корректность введенных данных")
            print(*titles[file])
            print(*args)
            print('''Нажмите Y если хотите сохранить введенные данные
Нажмите N если хотите отменить ввод
Нажмите E если хотите изменить данные''')
            n = input()
            if n in 'YyУу':
                with open(file, 'a', encoding='UTF-8') as out:
                    print(*args, sep=',', file=out)
                    print()
                    print('Данные успешно добавлены!')
                    print
                    break
            elif n in 'EeЕе':
                return func()
            elif n in 'Nn':
                print()
                print('Ввод отменен!')
                print
                break


#добавление в bus.txt
def add_bus():
        with open('bus.txt', 'r', encoding='UTF-8') as f:
            temp = max(enumerate(f.readlines(),1))[0]
        bus_id = 'bus' + str(temp + 1)
        bus_number = correctBusNumber()
        bus_model = input("Введите название модели автобуса>>>> ")
        bus_status = correctStatus()
        bus_route = chooseRoute()
        bus_driver = chooseDriver()
        add_info('bus.txt', add_bus, bus_id, bus_number, bus_model, bus_status, bus_driver, bus_route)


#добавление в driver.txt
def add_driver():
        with open('driver.txt', 'r', encoding='UTF-8') as f:
            temp = max(enumerate(f.readlines(),1))[0]
        driver_id = 'driver' + str(temp + 1)
        surname = correctName('фамилию')
        firstname = correctName('имя')
        fname = correctName('отчество')
        phone = correctPhoneNumber()
        while True:
            birth = birthDate()
            exp = timeWorkStart()
            if birth[1] >= 18 + exp[1]:
                break
            print("Стаж вождения не соответствует возрасту, проверьте информацию")
        add_info('driver.txt',add_driver, driver_id, surname, firstname, fname, birth[0], exp[1], phone)         

#добавление в bus.txt

def add_route():

    with open('routes.txt', 'r', encoding='UTF-8') as f:
        temp = max(enumerate(f.readlines(),1))[0]
    route_id = 'r' + str(temp + 1)
    route_num = enterRouteNumber()
    route_description = enterRoute()
    add_info('routes.txt', add_route, route_id, route_num, route_description)
