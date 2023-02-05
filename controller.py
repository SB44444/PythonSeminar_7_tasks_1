from os.path import exists
from list_filling import write_csv, write_txt, adding_data
from methods import create_file_csv, create_file_txt, screen

def start():
    text = input('Для начала работы нажмите любую букву\nДля выхода из программы любую цифру или символ - ')
    while text.isalpha() == True: # Если выбрана буква остаемся в меню выбора
        note_scv = 'Phonebook.csv'   # Присваиваем назвние файла для записи переменной  
        if exists(note_scv) == False: create_file_csv()  # Если файла для записи нет, создаем
        note_txt = 'Phonebook.txt'   # Присваиваем назвние файла для записи переменной  
        if exists(note_txt) == False: create_file_txt()  # Если файла для записи нет, создаем
        browse = input('Для записи нового контакта нажмите любую букву\nДля просмотра контактоа любую цифру или символ - ')
        if browse.isalpha() == True:  # Если выбрана буква, запускается добавление данных
            data = adding_data()  #  Присваиваем переменной результат функции
            write_csv(data)    #  Запуск ф-ций записи файла scv
            write_txt(data)    #  Запуск ф-ций записи файла txt
        else:
            screen()     #  Запуск ф-ций вывода файла
        text = input('Для продолжения нажмите любую букву\nДля выхода из программы любую цфру или символ - ')
    print('Работа программы завершена')
    