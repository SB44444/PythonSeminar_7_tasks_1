def adding_data():#  Ф-ция записи данных в список
    notes = []      #  Создаем список для записи
    phone_number = ''  #  Создаем строку для номера
    last_name = input('Запишите фамилию: ')   #  Записываем данные
    notes.append(last_name)
    first_name = input('Запишите имя: ')
    notes.append(first_name)    
    Flag = False
    while not Flag: #  Остаемся в меню, пока не набран нромер
        try:
            phone_number = input('Запишите номер телефона: ')
            if phone_number.isdigit() == False: print('В номере телефона могу быть только цифры')
            else:  #  Если все цифры - добавляем номер 
                Flag = True
        except: print('В номере телефона могу быть только цифры')
    notes.append(phone_number)
    comments = input('Запишите комментарий: ')
    notes.append(comments)
    return notes

def write_txt(notes):        #  Ф-ция добавления данных из списока в файл txt
    file2 = 'Phonebook.txt'
    with open(file2, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {notes[0]}\nИмя: {notes[1]}\nНомер телефона: {notes[2]}\nКомментарий: {notes[3]}\n\n')

def write_csv(notes):        #  Ф-ция добавления данных из списока в файл txt
    file1 = 'Phonebook.csv'
    with open(file1, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия  {notes[0]}; Имя  {notes[1]}; Номер телефона  {notes[2]}; Комментарий  {notes[3]}\n')
