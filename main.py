import os
import time

phonebook = {}

def actionText():
    actions = r'''
    Доступные команды для адресной книги:
    "Добавить" - Добавление контакта.
    "Просмотреть" - Просмотр имен всех контактов.
    "Открыть" - Открытие контакта.
    "Изменить" - Изменение контакта.
    "Удалить" - Удаление контакта.
    "Сохранить" - Сохранить все контакты в файл

    "Выход" - Завершение работы программы.
    '''
    print(actions)

def checkName(name):
    if name in phonebook:
        return True
    else:
        return False

def add():
    print()

    name = input('Введите имя контакта: ')
    phone_number = input('Введите номер телефона: ')
    print()

    if checkName(name):
        print('Ошибка: Контакт уже существует.')
    else:
        phonebook[name] = phone_number
        print('Контакт {} успешно добавлен!'.format(name))
    time.sleep(1.5)
    print()

def showAll():
    print()

    if len(phonebook) != 0:
        print('Доступные контакты:')
        for name in phonebook.keys():
            print(name)
    else:
        print('Ошибка: Адресная книга пуста.')
    time.sleep(1.5)
    print()

def openPerson():
    print()

    nameInput = input('Введите имя контакта: ')
    print()

    if checkName(nameInput):
        print('Номер телефона:\n' + phonebook.get(nameInput))
    else:
        print('Ошибка: Такого контакта нет в адресной строке.')
    time.sleep(1.5)
    print()

def change():
    print()
    
    nameToChange = input('Введите имя контакта для изменения: ')
    if checkName(nameToChange):
        strInput = input('Вы хотите изменить имя или телефон?\n').lower()
        if strInput == 'имя':
            newName = input('Введите новое имя: ')
            phone_number = phonebook.get(nameToChange)
            del phonebook[nameToChange]
            phonebook[newName] = phone_number
            print('\nКонтакт успешно изменён! Новый контакт:\n{} - {}'.format(newName, phonebook.get(newName)))
        elif strInput == 'телефон':
            phonebook[nameToChange] = input('Введите новый телефон: ')
            print('\nКонтакт успешно изменён! Новый контакт:\n{} - {}'.format(nameToChange, phonebook.get(nameToChange)))
        else:
            print('Ошибка: Введена неверная строка.')
    else:
        print("Ошибка: Введено неверное имя")
    time.sleep(1.5)
    print()

def delete():
    print()

    nameToDel = input('Введите имя контакта для удаления: ')
    if checkName(nameToDel):
        del phonebook[nameToDel]
        print('Контакт с именем {} успешно удалён.'.format(nameToDel))
    else:
        print('Ошибка: Контакта не существует')
    time.sleep(1.5)
    print()

def save():
    to_save = ""
    for k, v in phonebook.items():
        to_save += f'{k}    {v}\n'
    with open('phonebook.txt', 'w', encoding="utf-8") as file:
        file.write(to_save)
    print('До новых встреч!')
    quit()

def __init__():
    if os.path.isfile('phonebook.txt'):
        with open('phonebook.txt', encoding="utf-8") as file:
            members = file.readlines()
        for member in members:
            member = member.split()
            if member:
                phonebook[member[0]] = member[1]        

if __name__ == '__main__':
    __init__()
    print('\nДобро пожаловать в адресную книгу!')

    while True:
        actionText()
        line = input('>>> ').lower()
        if line == 'добавить':
            add()
            continue
        elif line == 'просмотреть':
            showAll()
            continue
        elif line == 'открыть':
            openPerson()
            continue
        elif line == 'изменить':
            change()
            continue
        elif line == 'удалить':
            delete()
            continue
        elif line == 'сохранить':
            save()
        elif line == "выход":
            print('До новых встреч!')
            break
        else:
            print('Ошибка: Неверная команда.')