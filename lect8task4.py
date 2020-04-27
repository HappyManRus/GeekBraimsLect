class warehouse:
    def __init__(self, room, rack, shelf):
        """
        Скалад
        :param room: комната/офис
        :param rack: стеллаж/кабинет
        :param shelf: полка/стол
        """
        self.room = room
        self.rack = rack
        self.shelf = shelf
        self.storigein = []

    def __str__(self):
        return f"{self.room}, {self.rack}, {self.shelf}"

    def add_eq(self, eqlinks):
        self.storigein.append(eqlinks)
        eqlinks.warehouse.clear()
        eqlinks.warehouse.append(self)

    def del_eq(self, eqlinks):
        self.storigein.remove(eqlinks)
        eqlinks.warehouse.clear()
        eqlinks.warehouse.append("перемещение")


class equipment:
    def __init__(self, types, model, quantity):
        """
        Оргтехника
        :param type: тип/наименование
        :param quantity: колличество
        """
        self.types = types
        self.model = model
        self.quantity = quantity
        self.warehouse = ["перемещение"]

    def add_to_storige(self, wrlinks):
        self.warehouse.append(wrlinks)

    def __str__(self):
        return (
            f"Тип оборудования {self.types}, модель {self.model}, колличество {self.quantity}, хранится {self.warehouse[0]}")


class printers(equipment):
    def __init__(self, types, model, quantity, speed):
        super().__init__(types, model, quantity)
        self.speed = speed

    @classmethod
    def add_printer(cls):
        try:
            anstype, ansmodel, ansspeed, ansquantity = map(str, input(
                "Введите тип, модель, скорость печати и колличество принтеров через пробел: ").split(' '))
            pr.append(printers(anstype, ansmodel, int(ansquantity), int(ansspeed)))
            if int(ansquantity) < 0:
                return False
        except:
            print("Ошибка в введенных данных. Колличество и скорость должны быть целым числом")
            return False
        print("Требуется определить место хранения или установки принтера.\nСписок помещений: ")
        print_all_warehouse()
        ansnum = input(
            "\033[31mПожалуйста введите номер помещения или нажмите Enter для установки статуса 'перемещение' : \033[0m")
        try:
            if int(ansnum) >= 0 and int(ansnum) <= len(wrlist):
                wrlist[int(ansnum)].add_eq(pr[len(pr) - 1])
            print("Создание успешно завершено. Вы создали:")
            print(pr[len(pr) - 1])
        except:
            print("ошибка привязки принтера, попробуйте позже, принтер сохранен с статусом 'перемещение'")

    @classmethod
    def move_printer(cls):
        print("Оборудование для перемещения:")
        print_all_printers()
        ansnumpr = input(
            "\033[31mПожалуйста введите номер оборудования для перемещения' : \033[0m")
        print("Требуется определить место хранения или установки принтера.")
        print("Список помещений: ")
        print_all_warehouse()
        ansnumwr = input(
            "\033[31mПожалуйста введите номер помещения или нажмите Enter для установки статуса 'перемещение' : \033[0m")
        anscolvo = input(
            "\033[31mПожалуйста введите колличество перемещаемых элементов : \033[0m")
        try:
            if int(ansnumwr) >= 0 and int(ansnumwr) <= len(wrlist) and int(ansnumpr) >= 0 and int(ansnumpr) <= len(
                    pr) - 1 and int(pr[int(ansnumpr)].quantity) >= int(anscolvo):
                pr.append(
                    printers(pr[int(ansnumpr)].types, pr[int(ansnumpr)].model, int(anscolvo), pr[int(ansnumpr)].speed))
                if pr[int(ansnumpr)].quantity - int(anscolvo) > 0:
                    pr[int(ansnumpr)].quantity = pr[int(ansnumpr)].quantity - int(anscolvo)
                else:
                    pr.pop(int(ansnumpr))
                print("Перемещение успешно завершено. Вы переместили:")
                wrlist[int(ansnumwr)].add_eq(pr[len(pr) - 1])
                print(pr[len(pr) - 1])
            else:
                print("Ошибка параметров перемещиения, попробуйте ещё раз")
                if int(pr[int(ansnumpr)].quantity) < int(anscolvo):
                    print("Перемещаете больше чем есть?")
        except:
            print("ошибка перемещения оборудования, попробуйте изменить параметры.")


class scaners(equipment):
    def __init__(self, types, model, quantity, ppti):
        super().__init__(types, model, quantity)
        self.ppti = ppti

    @classmethod
    def add_scaners(cls):
        try:
            anstype, ansmodel, ansppti, ansquantity = map(str, input(
                "Введите тип, модель, качество разрешения и колличество сканеров через пробел: ").split(' '))
            sc.append(printers(anstype, ansmodel, int(ansquantity), int(ansppti)))
            if int(ansquantity) < 0:
                return False
        except:
            print("Ошибка в введенных данных. Колличество и качество должны быть целым числом")
            return False
        print("Требуется определить место хранения или установки сканера.\nСписок помещений: ")
        print_all_warehouse()
        ansnum = input(
            "\033[31mПожалуйста введите номер помещения или нажмите Enter для установки статуса 'перемещение' : \033[0m")
        try:
            if int(ansnum) >= 0 and int(ansnum) <= len(wrlist):
                wrlist[int(ansnum)].add_eq(sc[len(sc) - 1])
            print("Создание успешно завершено. Вы создали сканер:")
            print(sc[len(sc) - 1])
        except:
            print("ошибка привязки сканера, попробуйте позже, сканер сохранен с статусом 'перемещение'")

    @classmethod
    def move_scaners(cls):
        print("Оборудование для перемещения:")
        print_all_scaners()
        ansnumsc = input(
            "\033[31mПожалуйста введите номер оборудования для перемещения' : \033[0m")
        print("Требуется определить место хранения или установки сканера.")
        print("Список помещений: ")
        print_all_warehouse()
        ansnumwr = input(
            "\033[31mПожалуйста введите номер помещения или нажмите Enter для установки статуса 'перемещение' : \033[0m")
        anscolvo = input(
            "\033[31mПожалуйста введите колличество перемещаемых элементов : \033[0m")
        try:
            if int(ansnumwr) >= 0 and int(ansnumwr) <= len(wrlist) and int(ansnumsc) >= 0 and int(ansnumsc) <= len(
                    sc) - 1 and int(sc[int(ansnumsc)].quantity) >= int(anscolvo):
                sc.append(
                    scaners(sc[int(ansnumsc)].types, sc[int(ansnumsc)].model, int(anscolvo), sc[int(ansnumsc)].ppti))
                if sc[int(ansnumsc)].quantity - int(anscolvo) > 0:
                    sc[int(ansnumsc)].quantity = sc[int(ansnumsc)].quantity - int(anscolvo)
                else:
                    sc.pop(int(ansnumsc))
                print("Перемещение успешно завершено. Вы переместили сканер:")
                wrlist[int(ansnumwr)].add_eq(sc[len(sc) - 1])
                print(sc[len(sc) - 1])
            else:
                print("Ошибка параметров перемещиения, попробуйте ещё раз")
                if int(sc[int(ansnumsc)].quantity) < int(anscolvo):
                    print("Перемещаете больше чем есть?")
        except:
            print("ошибка перемещения оборудования, попробуйте изменить параметры.")


class copirs(equipment):
    def __init__(self, types, model, quantity, size):
        super().__init__(types, model, quantity)
        self.speed = size

    @classmethod
    def add_copir(cls):
        try:
            anstype, ansmodel, anssize, ansquantity = map(str, input(
                "Введите тип, модель, размер и колличество копиров через пробел: ").split(' '))
            if int(ansquantity) < 0:
                return False
            cops.append(printers(anstype, ansmodel, int(ansquantity), int(anssize)))
        except:
            print("Ошибка в введенных данных. Колличество и скорость должны быть целым числом")
            return False
        print("Требуется определить место хранения или установки копира.\nСписок помещений: ")
        print_all_warehouse()
        ansnum = input(
            "\033[31mПожалуйста введите номер помещения или нажмите Enter для установки статуса 'перемещение' : \033[0m")
        try:
            if int(ansnum) >= 0 and int(ansnum) <= len(wrlist):
                wrlist[int(ansnum)].add_eq(cops[len(cops) - 1])
            print("Создание успешно завершено. Вы создали:")
            print(cops[len(cops) - 1])
        except:
            print("ошибка привязки принтера, попробуйте позже, копир сохранен с статусом 'перемещение'")

    @classmethod
    def move_copir(cls):
        print("Оборудование для перемещения:")
        print_all_copirs()
        ansnumcops = input(
            "\033[31mПожалуйста введите номер оборудования для перемещения' : \033[0m")
        print("Требуется определить место хранения или установки копира.")
        print("Список помещений: ")
        print_all_warehouse()
        ansnumwr = input(
            "\033[31mПожалуйста введите номер помещения или нажмите Enter для установки статуса 'перемещение' : \033[0m")
        anscolvo = input(
            "\033[31mПожалуйста введите колличество перемещаемых элементов : \033[0m")
        try:
            if int(ansnumwr) >= 0 and int(ansnumwr) <= len(wrlist) and int(ansnumcops) >= 0 and int(ansnumcops) <= len(
                    cops) - 1 and int(cops[int(ansnumcops)].quantity) >= int(anscolvo):
                cops.append(copirs(cops[int(ansnumcops)].types, cops[int(ansnumcops)].model, int(anscolvo),
                                   cops[int(ansnumcops)].speed))
                if cops[int(ansnumcops)].quantity - int(anscolvo) > 0:
                    cops[int(ansnumcops)].quantity = cops[int(ansnumcops)].quantity - int(anscolvo)
                else:
                    cops.pop(int(ansnumcops))
                print("Перемещение успешно завершено. Вы переместили:")
                wrlist[int(ansnumwr)].add_eq(cops[len(cops) - 1])
                print(cops[len(cops) - 1])
            else:
                print("Ошибка параметров перемещиения, попробуйте ещё раз")
                if int(cops[int(ansnumcops)].quantity) < int(anscolvo):
                    print("Перемещаете больше чем есть?")
        except:
            print("ошибка перемещения оборудования, попробуйте изменить параметры.")


def print_all_warehouse():
    print("Cписок всех складов и офисов")
    for i in range(len(wrlist)):
        print(str(i) + ". " + str(wrlist[i]))


def print_all_printers():
    print("Cписок всех принтеров с местом нахождения")
    for i in range(len(pr)):
        print(str(i) + ". " + str(pr[i]))


def print_all_scaners():
    print("Cписок всех сканеров с местом нахождения")
    for i in range(len(sc)):
        print(str(i) + ". " + str(sc[i]))


def print_all_copirs():
    print("Cписок всех копиров с местом нахождения")
    for i in range(len(cops)):
        print(str(i) + ". " + str(cops[i]))


wrlist = []
wrlist.append(warehouse("Комната 8", "Стеллаж 5", "Полка 4"))
wrlist.append(warehouse("Комната 3", "Стеллаж 1", "Полка 8"))
wrlist.append(warehouse("Офис 21", "Кабинет 15", "Стол 4"))
wrlist.append(warehouse("Офис 5", "Кабинет 1", "Стол 12"))

pr = []
pr.append(printers("laser", "hp512", 5, 10))
pr.append(printers("Stryiunii", "Epson", 3, 2))
wrlist[3].add_eq(pr[1])
wrlist[0].add_eq(pr[0])

sc = []
sc.append(scaners("table", "scan 123", 9, 100))
sc.append(scaners("line", "erix0n 1242", 7, 200))
wrlist[3].add_eq(sc[1])
wrlist[0].add_eq(sc[0])

cops = []
cops.append(copirs("Copir", "mod1", 1080, 3))
cops.append(copirs("Copir", "mod2", 720, 1))
wrlist[3].add_eq(cops[1])
wrlist[0].add_eq(cops[0])

while True:
    print("\n" * 25)
    print(
        "1. Добавить склад\n2. Добавить офис\n3. Добавить новое оборудование\n4. Переместить оборудование\n5. Просмотр списка всех складов и офисов\n6. Просмотр списка всего оборудования\n0. Выход\n")
    ans = input("Введите требуемое действие: ")
    if ans == "1":
        ansroom = input("Введите номер комнаты склада: ")
        ansrack = input("Введите номер стелажа в указанной комнате: ")
        ansshell = input("Введите номер полки в указанном стелаже: ")
        wrlist.append(warehouse("Комната " + str(ansroom), "Стеллаж " + str(ansrack), "Полка " + str(ansshell)))
    elif ans == "2":
        ansroom = input("Введите номер офиса: ")
        ansrack = input("Введите номер кабинета: ")
        ansshell = input("Введите номер стола: ")
        wrlist.append(warehouse("Офис " + str(ansroom), "Кабинет " + str(ansrack), "Стол " + str(ansshell)))
    elif ans == "3":
        ans_add = input("Вы хотите добавить:\n1. Принтер\n2. Сканер\n3. Копир. \nВведите номер обородования:  ")
        if ans_add == "1":
            printers.add_printer()
        elif ans_add == "2":
            scaners.add_scaners()
        elif ans_add == "3":
            copirs.add_copir()
        else:
            print("Ответ непонятен)")

    elif ans == "4":
        ans_add = input("Вы хотите переместить:\n1. Принтер\n2. Сканер\n3. Копир. \nВведите номер обородования:  ")
        if ans_add == "1":
            printers.move_printer()
        elif ans_add == "2":
            scaners.move_scaners()
        elif ans_add == "3":
            copirs.move_copir()
        else:
            print("Ответ непонятен)")

    elif ans == "5":
        print_all_warehouse()
    elif ans == "6":
        print_all_printers()
        print_all_scaners()
        print_all_copirs()
    elif ans == "0":
        break
    input("\033[31mНажмите Enter\033[0m")
