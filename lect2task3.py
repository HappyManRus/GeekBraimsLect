my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6:"Лето", 7:"Лето", 8:"Лето", 9:"Осень", 10:"Осень", 11:"Осень", 12:"Зима"}
my_list = ["Зима", "Зима","Весна", "Весна","Весна", "Лето", "Лето", "Лето", "Осень","Осень","Осень", "Зима"]
month_ask = int(input("Введите номер месяца : "))
print(f"Время года для месяца {month_ask} является {my_dict.get(month_ask)} (dict)")
print(f"Время года для месяца {month_ask} является {my_list[month_ask-1]} (list)")

#Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.