from controller import start
import os

clear = lambda: os.system('cls') # Очиста терминала
clear()
# os.system('cls')

def main(): # Функция запуска
    start() # Функция старта основной программы

if __name__ == '__main__':   # Проверка имени функции запуска программы
    main()