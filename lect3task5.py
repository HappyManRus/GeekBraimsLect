
summ = 0
while True:
    user_list = input("Enter the numbers with space - ").split()
    try:
        for element in user_list:
            summ +=int(element)
    except:
        break
    print (f"Сумма на данный момент: {summ}")

print (f"Итоговая сумма: {summ}")