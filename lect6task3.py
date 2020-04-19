class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return (self.name + " " + self.surname)

    def get_total_income(self):
        return (self._income.get('wage') + self._income.get('bonus'))


use_position = Position("David", "Coperfild", "Director", 300, 150)
print(
    f"Наш клиент по имени {use_position.get_full_name()} имеет доход {use_position.get_total_income()} тугриков в месяц, до вычита налогов")

use_position_2 = Position("Vladimir", "Zirinovskii", "Кандидат в президенты", 10, 99999)
print(
    f"Наш клиент по имени {use_position_2.get_full_name()} имеет доход {use_position_2.get_total_income()} тугриков в месяц, до вычита налогов")
print(f"Он работвет в должности {use_position_2.position}")
