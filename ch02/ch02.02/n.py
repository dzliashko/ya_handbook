# Во времена, когда люди верили в магическую силу чисел, волшебник Пифуман
# предал все народы и встал на сторону Зерона.

# Теперь, чтобы проникнуть в башни обоих злодеев одновременно, нужно разделить
# силу числа, которое защищало нас в дороге.

# Для этого возьмём трёхзначное число и составим из него минимальное и
# максимальное возможные двухзначные числа.

# Формат ввода
# Одно трёхзначное число.

# Формат вывода
# Два защитных числа для каждого отряда, записанные через пробел.

# Подсказка
# Пример 1
# Ввод
# 103
# Вывод
# 10 31
# Пример 2
# Ввод
# 787
# Вывод
# 77 87

s = input().strip()
a, b, c = s[0], s[1], s[2]

min_val = None
max_val = None

# Комбинация 1: a + b
if a != "0":
    num = int(a + b)
    if min_val is None:
        min_val = num
        max_val = num
    else:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

# Комбинация 2: a + c
if a != "0":
    num = int(a + c)
    if min_val is None:
        min_val = num
        max_val = num
    else:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

# Комбинация 3: b + a
if b != "0":
    num = int(b + a)
    if min_val is None:
        min_val = num
        max_val = num
    else:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

# Комбинация 4: b + c
if b != "0":
    num = int(b + c)
    if min_val is None:
        min_val = num
        max_val = num
    else:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

# Комбинация 5: c + a
if c != "0":
    num = int(c + a)
    if min_val is None:
        min_val = num
        max_val = num
    else:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

# Комбинация 6: c + b
if c != "0":
    num = int(c + b)
    if min_val is None:
        min_val = num
        max_val = num
    else:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

print(f"{min_val} {max_val}")
