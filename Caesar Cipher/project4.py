# Шифр Цезаря
# Описание проекта: требуется написать программу,
# способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
# Она должна запрашивать у пользователя следующие данные:
#
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).
#
# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
# Примечание 3. Сохраните регистр символов. Например, текст:
# "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
#
# Составляющие проекта:
# Целые числа (тип int);
# Модульная арифметика;
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for/while;
# Строковые методы.


def decryption(language, shift, w_text):
    for i in range(len(w_text)):
        if language == 'а' or language == 'a' or language == 'en':
            if w_text[i] in ' ,.!-?`':
                print(text[i], end='')
            elif w_text[i] not in ' ,.!-?`':
                print(chr(ord(w_text[i]) - shift), end='')
        elif language == 'р' or language == 'r' or language == 'rus':
            if w_text[i] in ' ,.!-?`':
                print(text[i], end='')
            elif w_text[i] not in ' ,.!-?`':
                print(chr(ord(w_text[i]) - shift), end='')
        else:
            print('Введены некоректные данные')


def encryption(language, shift, w_text):
    for i in range(len(w_text)):
        if language == 'а' or 'a' or 'en':
            if w_text[i] in ' ,.!-?`':
                print(text[i], end='')
            elif w_text[i] not in ' ,.!-?`':
                print(chr(ord(w_text[i]) + shift), end='')
        elif language == 'р' or 'r' or 'rus' and w_text[i] not in ' ,.!-?`':
            if w_text[i] in ' ,.!-?`':
                print(text[i], end='')
            elif w_text[i] not in ' ,.!-?`':
                print(chr(ord(w_text[i]) + shift), end='')
        else:
            print('Введены некоректные данные')


print('-' * 60)
print('Привет мир, это приложение для шифрования или дешифрования предложений. \nШифрование будет делаться методом подстановки(Шифром Цезаря)')
print('-' * 60)
whats_direction = input('Напишите направление: шифрование - [ш] или дешифрование - [д]: ').lower()
whats_language = input('Выберите язык алфавита: русский - [р] или английский - [а]: ').lower()
whats_shift = int(input('Выберите шаг сдвига (со сдвигом вправо): '))
text = input('Поля для ввода текста: ')

print('-' * 60)
if whats_direction == 'ш' or whats_direction == '1' or whats_direction == 'шифрование':
    print('Зашифрованный текст:', end='')
    encryption(whats_language, whats_shift, text)
elif whats_direction == 'д' or whats_direction == '2' or whats_direction == 'дешифрование':
    print('Дешифрованный текст:', end='')
    decryption(whats_language, whats_shift, text)
else:
    print('Введены некоректные данные! ')
