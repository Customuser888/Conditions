from math import sqrt
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

d = b**2-4*a*c
if d > 0:
  print ('У Уравнения 2 Корня:')
  x1 = (-b + sqrt(d)) / (2 * a)
  x2 = (-b - sqrt(d)) / (2 * a)
  print (f'X1 = {x1} X2 = {x2}')
if d==0:
  print ('У Уравнения 1 Корень:')
  x1 = -b / (2 * a)
  print (f'X = {x1}')
else:
  print ('У Уравнения Нет Корней:')