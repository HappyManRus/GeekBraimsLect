import re

mydict = {}
try:
    fread = open("text_6.txt", encoding='utf-8')
    for line in fread:
        match = re.findall(r'(\w+|\d+)[:|(]', line)
        mydict[match[0]] = sum(int(i) for i in match[1:])
    print(mydict)
except IOError:
    print("Произошла ошибка ввода-вывода!")
except:
    print("Некоректные данные!")
