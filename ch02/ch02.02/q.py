# найдём корни уравнения, используя составные условные операции.

# Формат ввода
# Вводится 3 вещественных числа a, b, c — коэффициенты уравнения вида:

# a * x**2 + b * x + c = 0.

# Формат вывода
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке
# возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».

# Примечание
# Обратите внимание: ограничения на значения коэффициентов отсутствуют.


# Рассмотрите варианты:

# все коэффициенты равны нулю;
# коэффициенты a и b равны нулю;
# только коэффициент a равен нулю;
# коэффициент a не равен нулю.

# Подсказка
# Пример 1
# Ввод
# 1
# -2
# 1
# Вывод
# 1.00
# Пример 2
# Ввод
# 3.5
# -2.4
# -7.3
# Вывод
# -1.14 1.83
import math


a = float(input().strip())
b = float(input().strip())
c = float(input().strip())

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0:
    print("No solution")
elif a == 0:
    root = -c / b
    print(f"{root:.2f}")
else:
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        print("No solution")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"{root:.2f}")
    else:
        sqrt_d = math.sqrt(discriminant)
        root1 = (-b - sqrt_d) / (2 * a)
        root2 = (-b + sqrt_d) / (2 * a)
        root1, root2 = sorted([root1, root2])
        print(f"{root1:.2f} {root2:.2f}")
