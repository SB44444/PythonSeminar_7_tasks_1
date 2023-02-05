def reading_data(file):  #  Ф-ция чтения из файла
    with open(file, 'r+', encoding='utf-8') as data:
        read_file = data.read()
    return read_file

def create_file_csv():   #  Ф-ция записи файла
    file = 'Phonebook.csv'
    with open(file, 'w+', encoding='utf-8') as data:
        data.write('ТЕЛЕФОННАЯ КНИГА\n')

def create_file_txt():   #  Ф-ция записи файла
    file = 'Phonebook.txt'
    with open(file, 'w+', encoding='utf-8') as data:
        data.write('\n')

def screen():   #  Ф-ция вывода данных в терминал
    view = input('Для отображения контактых данных в строку нажмите любую букву\nДля вывода блоками нажмите любую цифру или символ - ')
    if view.isalpha() == True: print(reading_data('Phonebook.csv'))
    else:
        print(reading_data('Phonebook.txt'))
