''' Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) 
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.'''
import collections


enterprises = {}

s = int(input('Введите колличество предприятий:'))
a = collections.namedtuple('enterprise_n', ['b1', 'b2', 'b3', 'b4'])

for i in range(s):
    name = input(str(i + 1) + 'Название предприятия:')
    income1 = int(input('Доход данного предприятия за 1 квартал:'))
    income2 = int(input('Доход данного предприятия за 2 квартал:'))
    income3 = int(input('Доход данного предприятия за 3 квартал:'))
    income4 = int(input('Доход данного предприятия за 4 квартал:'))
     
    enterprises[name] = a(b1 =income1, b2 = income2, b3 = income3, b4 = income4)
    
print(f'Организации и их доход: {enterprises}')
sum_income = ()
for key, value in enterprises.items():
    print(f'Предприятие:{key} , сумма его доходов за год: {sum(value)}')
    sum_income += value



medium = sum(sum_income) / len(enterprises)

print(f'Среднее значение прибыли предприятий {medium}')

low = {}
high = {}

for key, value in enterprises.items():
    if sum(value) > medium:
        high[key] = sum(value)
    else:
        low[key] = sum(value)

print(f'Предприятия, доход которых ниже среднего:{low}')

print(f'Предприятия, доход которых выше среднего:{high}')
