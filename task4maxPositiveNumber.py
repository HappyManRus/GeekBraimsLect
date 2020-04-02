input_number = int(input("Введите целое положительное число : "))
max_number = input_number % 10
input_number = input_number // 10

while input_number > 0:
    if max_number == 9: break
    if (input_number % 10) > max_number: max_number = (input_number % 10)
    input_number = input_number // 10

print(f"Самая большая цифра в числе {max_number}")

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
