class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите делимое: ")
inp_data2 = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    inp_data2 = int(inp_data2)
    if inp_data2 == 0:
        raise OwnError("Деление на нуль невозможно!")
    res = inp_data / inp_data2
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления первого числа на второе: {round(res, 2)}")
