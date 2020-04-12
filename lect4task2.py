import random

new_list = [random.randint(0, 10) for i in range(10)]
new_list2 = [new_list[i + 1] for i in range(len(new_list) - 1) if new_list[i] < new_list[i + 1]]
print(f"Начальный список: {new_list}")
print(f"Измененый список: {new_list2}")
