class date_class:
    def __init__(self, str):
        self.str = str

    def data_convert_and_check(self):
        return date_class.date_parserMap(self.str)

    @classmethod
    def date_parserMap(cls, datestr):
        day, month, year = map(int, datestr.split('-'))
        return cls.date_check(year, month, day)

    @staticmethod
    def date_check(paryear, parmonth, parday):
        if (paryear < 1999) or (paryear > 2100):
            paryear = 1999
        if (parmonth < 1) or (parmonth > 12):
            parmonth = 1
        if (parday < 1) or (parday > 31):
            parday = 1
        return (paryear, parmonth, parday)


dt = date_class("27-03-2020")
try:
    print(f"Массив с проверенными элементами даты (YYYY, MM, DD): {dt.data_convert_and_check()}")
except:
    print("Неверный формат даты")
