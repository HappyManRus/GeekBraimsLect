class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


mylist = []

while True:
    try:
        data_user = input("Введите число. Для завершения введите stop: ")
        if data_user == "stop":
            break
        if not data_user.isdigit():
            raise OwnError("Число введено некорректно!")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        mylist.append(data_user)

print(mylist)
