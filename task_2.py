a = int(input("Укажите делимое: "))
b = int(input("Укажите делитель: "))
def s_calc(a, b):
    try:
        return a/b
    except ZeroDivisionError as s_calc:
        print('Вы что? Пытаетесь делить на 0')
print(s_calc(a, b))
