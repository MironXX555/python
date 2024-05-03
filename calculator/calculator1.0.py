print("Привет дорогой друг! Я - Мирон! И я создал калькулятор. Потом буду создавать что то посложнее!!!")
print("Выбери действие!!")
print("1 - Сложение")
print("2 - Вычитание")
print("3 - Умножение")
print("4 - Деление")
tip_deystviya = int(input("Введи номер действия: "))
num1 = int(input("Введи первое число: "))
num2 = int(input("Введи второе число: "))
if tip_deystviya == 1:
  print("Твой пример:", num1, "+", num2, "Равно:", num1 + num2)
elif tip_deystviya == 2:
  print("Твой пример:", num1, "-", num2, "Равно:", num1 - num2)
elif tip_deystviya == 3:
  print("Твой пример:", num1, "x", num2, "Равно:", num1 *  num2)
elif tip_deystviya == 4:
  print("Твой пример:", num1, "/", num2, "Равно:", num1 / num2)
else:
  print("Числа не делятся на 0!!!")
