a = int(input('Введите Число 1: '))
b = int(input('Введите Число 2: '))
c = int(input('Введите Число 3: '))

if a==b or a==c or c==b:
  print('Ошибка!!11!1')

elif (a < b and a > c) or (a < c and a > b):
 print (f'Среднее число = {a}')

elif (b < a and b > c) or (b < c and b > a): 
 print (f'Среднее число = {b}')
 
else: 
  print (f'Среднее число = {c}')