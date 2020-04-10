def my_func(x, y):
    """
    Функция возведения в отрицательную степень
    :param x: всегда должно быть целое положительное
    :param y: всегда должно быть целое отрицательное
    :return: возвращает x в отрицательной степени y
    """

    temp_x = 1;
    for i in range(0, y, -1):
        temp_x *= x
    return (1 / temp_x)


def my_func_classic(x, y):
    return (x ** y)


try:
    x = int(input("Введите положительное число Х: "))
    y = int(input("Введите отрицательное число y: "))
    if x > 0 and y < 0:
        print(my_func(x, y))
        print(my_func_classic(x, y))
        print((lambda x_l, y_l: x_l ** y_l)(x, y))
    else:
        print('Вы ввели цифры, но с неверным знаком или равные нулю.')
except:
    print("Вы ввели неверные данные.")
