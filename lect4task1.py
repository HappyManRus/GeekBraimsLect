def my_salary(pr_hours, pay_hours, bonus_p):
    try:
        return (int(pr_hours) * int(pay_hours)) + int(bonus_p)
    except:
        return "расчет невозможен, неверные входные параметры"


from sys import argv

script_name, prod_in_hours, pay_in_hours, bonus = argv
print("Сумма ЗП: ", my_salary(prod_in_hours, pay_in_hours, bonus))
