def my_data(name, fam, years, city, email, phone):
    return (name + " " + fam + " " + years + " " + city + " " + email + " " + phone)


fio_name = input("Введите Имя: ")
fio_fam = input("Введите Фамилию: ")
fio_year = input("Введите Год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите Email: ")
phone = input("Введите номер телефона: ")

print(
    f"Сумарная строка персональных данных: {my_data(name=fio_name, fam=fio_fam, years=fio_year, city=city, email=email, phone=phone)}")
