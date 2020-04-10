def check_letter(string_for_check):
    for letter in string_for_check:
        if not letter in "abcdefghjklmnopqrstuvwxyzABCDEFGHJKLMNOPRQRSTUVWXYZ":
            return False
    return True


def int_func(string_for_up):
    """
    Функция преобразования первого символа строки в верхний регистр
    :param string_for_up: строка для преобразования
    :return: строка с большой первой буковй
    """
    if check_letter(string_for_up):
        string_for_up = string_for_up.replace(string_for_up[0], string_for_up[0].upper(), 1)
        return string_for_up
    else:
        return f"Ошибка_слово_'{string_for_up}'_было_не_только_из_латинских_букв"


print(int_func("tRaTp"))

user_list = input("Enter the words with space - ").split()
new_str = ""
for element in user_list:
    new_str += int_func(element) + " "

print(new_str.strip())

# Сделал чётко по заданию, "функцию int_func(), принимающую слово из маленьких латинских букв ".
# Но более логично былобы фильтровать слова на этапе ввода, до основной части, например бесконечным циклом, пока пользователь не введёт строку только из латинских букв.
