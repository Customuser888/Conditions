a = int(input('Введите Число 1: '))
b = int(input('Введите Число 2: '))
c = int(input('Введите Число 3: '))

if a > b and a > c:
  print (f'Самое большое число = {a}')
elif b > a and b > c:
  print (f'Самое большое число = {b}')
else: 
  print (f'Самое большое число = {c}')