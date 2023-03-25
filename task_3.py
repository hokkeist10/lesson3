name = input("Укажите Имя: ")
surname = input("Укажите фамилию: ")
year = input("Укажите год рождения: ")
city = input("Укажите город проживания: ")
email = input("Укажите почту: ")
phone_number = input("Укажите номер телефона: ")
def my_func(var_1, var_4, var_6, var_3, var_2, var_5):
    print(f'{var_1} {var_2} {var_3} года рождения, проживает в городе {var_4}, email:{var_5}, телефон {var_6}')
my_func(var_1=name, var_4=city, var_6=phone_number, var_3=year, var_2=surname, var_5=email)