a = int(input("Дальность Выстрела: "))

if a > 28 and a < 30:
  print("ПОПАЛ")
elif a >= 30:
  print("ПЕРЕЛЕТ")
elif a > 0 and a <= 28:
  print("НЕДОЛЕТ")
elif a <= 0:
  print("НЕ БЕЙ ПО СВОИМ")