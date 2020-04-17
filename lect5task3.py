try:
    f = open("text_3.txt", encoding='utf-8')
    total = 0
    for i, line in enumerate(f):
        listline = line.split()
        if float(listline[1]) < 20000:
            print(f"{listline[0]} имеет зарплату {listline[1]} - она ниже 20000")
        total += float(listline[1])
    print(f"Средняя зарплата по палате = {round(total / (i + 1), 2)}")
    f.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
except:
    print("Некоректные данные!")

# enumerate использовал для примера, что тоже умею им пользоваться) Понимаю что не красиво и опасно переменную i использовать вне цикла.
