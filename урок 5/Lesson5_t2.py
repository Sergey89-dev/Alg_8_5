''' Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. 
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. 
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''
from  collections import Counter
import collections
a = input('Введите шестнадцатиричное число:')
two = input('Введите второе шестнадцатиричное число:')
a = a.upper()
two = two.upper()
a = list(a.strip())
two = list(two.strip())
user = collections.Counter()
for i in a:
    user[i] += 1

for i in two:
    user[i] += 1

b = Counter(a)
c = Counter(two)

col1 = list(b.elements())
col2 = list(c.elements())

print(col1)
print(col2)
numb = {'A':10, 'B':11, 'C':12, 'D':13, 'C':14, 'F':15}
def numb_func(n):
    for i in range(len(n)):
        if n[i] == 'A':
            n[i] = 10
        elif n[i] == 'B':
            n[i] = 11
        elif n[i] == 'C':
            n[i] = 12
        elif n[i] == 'D':
            n[i] = 13
        elif n[i] == 'E':
            n[i] = 14
        elif n[i] == 'F':
            n[i] = 15
        elif n[i] == '0':
            n[i] = 0
        elif n[i] == '1':
            n[i] = 1
        elif n[i] == '2':
            n[i] = 2
        elif n[i] == '3':
            n[i] = 3
        elif n[i] == '4':
            n[i] = 4
        elif n[i] == '5':
            n[i] = 5
        elif n[i] == '6':
            n[i] = 6
        elif n[i] == '7':
            n[i] = 7
        elif n[i] == '8':
            n[i] = 8
        elif n[i] == '9':
            n[i] = 9
    return n

def numb_func16(a):
    for n in range(len(a)):
        if a[n] == 10:
            a[n] = 'A'
        elif a[n] == 11:
            a[n] = 'B'
        elif a[n] == 12:
            a[n] = 'C'
        elif a[n] == 13:
            a[n] = 'D'
        elif a[n] == 14:
            a[n] = 'E'
        elif a[n] == 15:
            a[n] = 'F'
        elif a[n] == 0:
            a[n] = '0'
        elif a[n] == 1:
            a[n] = '1'
        elif a[n] == 2:
            a[n] = '2'
        elif a[n] == 3:
            a[n] = '3'
        elif a[n] == 4:
            a[n] = '4'
        elif a[n] == 5:
            a[n] = '5'
        elif a[n] == 6:
            a[n] = '6'
        elif a[n] == 7:
            a[n] = '7'
        elif a[n] == 8:
            a[n] = '8'
        elif a[n] == 9:
            a[n] = '9'
    return a
def numb_func10(a):
    a2 = numb_func(a)
    b = 0
    for i in range(len(a2)):
        length = len(a2) - i - 1
        s = 16 ** length
        proc = int(a2[i]) * s
        b += proc
    return b

def sum_numb(a,b):
    s = []
    a2 = numb_func(a[::-1])
    b2 = numb_func(b[::-1])
    if len(a2) >= len(b2):
        for i in range(len(a2) - len(b2)):
            b2.append(0)
    else:
        for i in range(len(b2) - len(a2)):
            a2.append(0)
    n, m2, m3 = 0, 0, 0
    for i in range(len(a2)):
        m2 = int(a2[i]) + int(b2[i]) + n
        if m2 >= 16:
            n = m2 // 16
            m3 = m2 % 16
        else:
            m3 = m2
            n = 0
        s.append(m3)
    if n > 0:
        s.append(n)
    
    return numb_func16(s[::-1])

def mult_func(a, b):
    n = a
    for i in range(numb_func10(b)-1):
        n = sum_numb(a, n)
    return n

sumn = sum_numb(a, two)
multn = mult_func(a, two)
print(f'Cумма введенных шестнадцатиричных чисел: {col1} + {col2} = {sumn}')
print(f'Произведение введенных шестнадцатиричных чисел: {col1} * {col2} = {multn}')



