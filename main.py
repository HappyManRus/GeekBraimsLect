timesecinput = int(input("Введите время в секундах: "))
timehours = timesecinput // 3600
timeminuts = (timesecinput % 3600) // 60
timesec = (timesecinput % 3600) % 60
print("Время в удобном формате: {:02d}:{:02d}:{:02d}".format(timehours, timeminuts, timesec))
