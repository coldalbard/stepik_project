import random


def check_password(count_p, numbers, u_case, l_case, s_case):
    chars = ''
    if count_p >= 1:
        if numbers == 'да' or numbers == '+' or numbers == 'yes':
            chars += digits
        if u_case == 'да' or u_case == '+' or u_case == 'yes':
            chars += uppercase_letters
        if l_case == 'да' or l_case == '+' or l_case == 'yes':
            chars += lowercase_letters
        if s_case == 'да' or s_case == '+' or s_case == 'yes':
            chars += punctuation
    return chars


def create_password(p_lenght, chars):
    password = ''
    for j in range(p_lenght):
        password += chars[random.randint(0, len(chars) - 1)]
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
print('Привет мир!, это программа для генерации безопасных поролей')
count_pas = int(input('Введите количество паролей: '))
count_password_size = int(input('Введите длину одного пароля: '))
on_digit = input('Включать ли цифры 0123456789?: ').lower()
on_uppercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?: ').lower()
on_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?: ').lower()
on_symbols = input('Включать ли символы !#$%&*+-=?@^_?: ').lower()


pas_chars = check_password(count_pas, on_digit, on_uppercase, on_lowercase, on_symbols)
for i in range(1, count_pas + 1):
    print(f'{i}. {create_password(count_password_size, pas_chars)}')
