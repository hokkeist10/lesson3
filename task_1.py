dict = {1:'Зима',
        2:'Зима',
        3:'Весна',
        4:'Весна',
        5:'Весна',
        6:'Лето',
        7:'Лето',
        8:'Лето',
        9:'Осень',
        10:'Осень',
        11:'Осень',
        12:'Зима'
}
number = int(input('Введите номер месяца: '))
period = dict[number]
print(f'Результат через словарь: {period}')

periods = ['Зима', 'Весна', 'Лето', 'Осень']
if number == 1 or number == 2 or number == 12:
        print(f'Результат через список: {periods[0]}')
elif number == 3 or number == 4 or number == 5:
        print(f'Результат через список: {periods[1]}')
elif number == 6 or number == 7 or number == 8:
        print(f'Результат через список: {periods[2]}')
else:
        print(f'Результат через список: {periods[3]}')
