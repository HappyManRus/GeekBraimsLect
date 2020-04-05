mystruct = []
new_list = []
new_dict = {}

input_num = 1
while True:
    item_name = input("Введите название товара (пустую для окончания ввода): ")
    if item_name == "":
        break
    item_price = float(input("Введите цену товара : "))
    item_count = int(input("Введите колличество товара : "))
    item_type = input("Введите ежиницу измерения товара : ")
    mystruct.append((input_num, {"название": item_name, "цена": item_price, "количество": item_count, "eд": item_type}))
    input_num += 1

print(mystruct)

for element_tuple in mystruct:
    for elm_keys in element_tuple[1].keys():
        if new_dict.get(elm_keys) is None:
            new_list.clear()
        else:
            new_list = new_dict[elm_keys].copy()
        new_list.append(element_tuple[1].get(elm_keys))
        new_dict.update({elm_keys: list(set(new_list.copy()))})
print(new_dict)

# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# mystruct = [
#    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
# ]
