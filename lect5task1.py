try:
    f = open("my_file_task1.txt", 'w')
    while True:
        str_text = input("Введите строку, для окончания просто нажмите Enter: ")
        if str_text == "":
            break
        f.write(str_text + "\n")
    f.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
