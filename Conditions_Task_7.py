import math
x = int(input('Выберите Фигуру(1-Прямоугольник 2-Треугольник 3-Круг): '))


if x==1:
  a = int(input('1я Сторона Прямоугольника: '))
  b = int(input('2я Сторона Прямоугольника: '))
  S = a * b
  print(f'Площадь Прямоугольника: {S}')
if x==2:
  a = int(input('Основание Треугольника: '))
  b = int(input('Высота Треугольника: '))
  S = 0.5 * a * b
  print(f'Площадь Тремоугольника: {S}')
if x==3:
  r = int(input('Радиус Круга: '))
  S = math.pi * r ** 2
else:
  print('Набери Нормально, Такого Варианта Нет¯\_(ツ)_/¯')