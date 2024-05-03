import math

print("Привет! Я написал вторую версию моего калькулятора.")
print("Я могу выполнять следующие операции:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Вычисление остатка от деления")
print("7. Вычисление целой части от деления")
print("8. Вычисление квадратного корня")
print("9. Вычисление кубического корня")
print("10. Вычисление факториала")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operation = int(input("Введите номер операции: "))
if operation == 1:
    print(num1 + num2)
elif operation == 2:
    print(num1 - num2)
elif operation == 3:
    print(num1 * num2)
elif operation == 4:
    print(num1 / num2)
elif operation == 5:
    print(num1 ** num2)
elif operation == 6:
    print(num1 % num2)
elif operation == 7:
    print(num1 // num2)
elif operation == 8:
    print(num1 ** (1/2))
elif operation == 9:
    print(num1 ** (1/3))
elif operation == 10:
    print(math.factorial(num1))
