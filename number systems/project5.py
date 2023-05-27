def check_sys_number():
    flag = False
    while flag == False:
        print()
        print('Напоминаем, что мы переводим из 10-й системы счисления в 2-ю, 8-ю и 16-ю\nЧтобы выбрать 2-ю систему напишите - [2], в 8-ю - [8], в 16-ю - [16]')
        number = input('Введите систему счисления: ')
        if number.isdigit() and number in '2 8 16'.split():
            flag = True
            return int(number)
        else:
            print('Введены некоректные данные!')


def check_user_number():
    flag = False
    print()
    while flag == False:
        number = input('Введите число которое хотите перевести в одну из систем счисления: ')
        if number.isdigit():
            flag = True
            return int(number)
        else:
            print('Введены некоректные данные!')


def num_system():
    print('Привет мир, вы в программе для перевода чисел из десятичной системы счисления в другие.')
    print('-'*90)
    sys_number = check_sys_number()
    user_number = check_user_number()
    if sys_number == 2:
        print(bin(user_number)[2:])
    elif sys_number == 8:
        print(oct(user_number)[2:])
    elif sys_number == 16:
        print((hex(user_number)[2:]).upper())


num_system()
