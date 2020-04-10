def my_devide(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except:
        return "Неделится, нуль второй?"


try:
    first_num = float(input("Введите первое число : "))
    second_num = float(input("Введите второе число : "))
    print(f"Результат деления: {my_devide(first_num, second_num)}")
except:
    print("А вы точно число ввели? А?")
