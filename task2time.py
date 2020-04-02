timesec_input = int(input("Введите время в секундах: "))
time_hours = timesec_input // 3600
time_minuts = (timesec_input % 3600) // 60
time_sec = (timesec_input % 3600) % 60
print("Время в удобном формате: {:02d}:{:02d}:{:02d}".format(time_hours, time_minuts, time_sec))
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
