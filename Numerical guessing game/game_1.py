import random

# Угадайка чисел
# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100
# и просит пользователя угадать это число. Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа,
# то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число,
# то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл while;
# Бесконечный цикл;
# Операторы break, continue;
# Работа с модулем random для генерации случайных чисел.


print("Приветствую вас в игре Угадайка чисел!\nПравила игры просты: компьютер случайным образом генерирует число\n"
          "от 1 до 100, вашей задачей является угадать какое число было загадано компьютером. Желаю удачи!)\n")


def range_number():
    print('Хотите ли ввести диапозон чисел, в котором компьютер создаст секретное число?\nЕсли да, то введите - [да].'
          'В противном случае диапозон бедет равен [1:100]')
    diapozon = input('Поле для ввода: ').lower()
    if diapozon == 'да':
        flag = False
        while flag == False:
            left = input('Ввидите число, которое будет началом диапозона: ')
            right = input('Ввидите число, которое будет концом диапозона: ')
            if left.isdigit() and right.isdigit() and int(left) < int(right):
                flag = True
                g_number = random.randint(int(left), int(right))
                return g_number, int(left), int(right)
            else:
                print('Напоминаю вам, что границы диапозона должны быть целыми числами. \nИ еще начало диапозона должна быть меньше его конца.\n')
    else:
        g_number = random.randint(1, 100)
        return g_number, 1, 100




def correct_number(text, lf_r, r_r):
    flag = False
    while flag == False:
        if text.isdigit() and lf_r <= int(text) <= r_r:
            flag = True
            return int(text)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?\n')
            text = input('Введите предполагаемое число: ')


def comparison(secret_number, left_r, right_r):
    flag = False
    count_n = 0
    more = ['Слишком много, попробуйте еще раз\n', 'Это число явно меньше\n', 'Может взять по меньше?\n']
    less = ['Мало(\n', 'Может возьмём по больше?\n', 'Думаю, наше число явно по больше\n', 'Я бы взял по больше\n']
    while flag == False:
        count_n += 1
        int_text = correct_number(input('Введите предполагаемое число: '), left_r, right_r)
        if int_text == secret_number:
            print(f'В точку, вы угадали с {count_n} попытки. Примите мои поздравлениея!\n')
            print('Хотите сыграть повторно?')
            game_reboot = input('Введите [да] или [нет]: ').lower()
            print()
            if game_reboot == 'нет' or game_reboot != 'да':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                flag = True
            else:
                count_n = 0
                secret_number, left_r, right_r = range_number()
                print('Новое число готово. \n')
        elif secret_number > int_text:
            print(less[random.randint(0, len(less)) - 1])
        elif int_text > secret_number:
            print(more[random.randint(0, len(more)) - 1])
        else:
            count_n -= 1


guessed_number, left_range, right_range = range_number()
comparison(guessed_number, left_range, right_range)