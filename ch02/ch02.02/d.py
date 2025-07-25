# Время подвести итоги гонки и объявить победителя!
# Длина трассы — 43872 метра, и нам известны средние скорости трёх фаворитов:
# Пети, Васи и Толи.
# Ваша задача — сравнить результаты гонщиков и вывести имя победителя.

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Имена победителей в порядке занятых мест.

# Подсказка
# Пример 1
# Ввод
# 10
# 5
# 7
# Вывод
# 1. Петя
# 2. Толя
# 3. Вася
# Пример 2
# Ввод
# 5
# 7
# 10
# Вывод
# 1. Толя
# 2. Вася
# 3. Петя

first_name = "Петя"
first_speed = float(input())
second_name = "Вася"
second_speed = float(input())
third_name = "Толя"
third_speed = float(input())

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

print(f"1. {first_name}\n2. {second_name}\n3. {third_name}")
