import json

mydict = {}
profit = 0
profitTotal = 0
count_profit = 0
finallist = []
try:
    with open("text_7.txt", encoding='utf-8') as f_obj:
        for line in f_obj:
            str_firm = line.split()
            profit = int(str_firm[2]) - int(str_firm[3])
            mydict[str_firm[0]] = profit
            if profit > 0:
                profitTotal += profit
                count_profit += 1

    finallist.append(mydict)
    finallist.append({"average_profit": (round(profitTotal / count_profit, 1))})
    with open("my_file.json", "w", encoding='utf-8') as write_f:
        json.dump(finallist, write_f, ensure_ascii=False, indent=4)
except IOError:
    print("Произошла ошибка ввода-вывода!")
except:
    print("Некоректные данные!")
