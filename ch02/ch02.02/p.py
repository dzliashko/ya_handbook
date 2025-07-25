# Осталось ещё 4 задачи! Давайте освежим в памяти, как работать с вложенными
# условными операторами if-else или if-elif-else и применять наивную
# сортировку данных.

# В новом сезоне за первенство в велогонках снова сражаются сильнейшие.
# Протяжённость финальной трассы — 43872м, и все хотят узнать, кто первым
# пересечёт финишную черту.

# Нам известны средние скорости трёх претендентов — Пети, Васи и Толи. Кто
# станет победителем?

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Красивый пьедестал (ширина ступеней 8 символов).

# Подсказка
# Пример 1
# Ввод
# 10
# 5
# 7
# Вывод
#           Петя
#   Толя
#                   Вася
#    II      I      III
# Пример 2
# Ввод
# 5
# 7
# 10
# Вывод
#           Толя
#   Вася
#                   Петя
#    II      I      III

first_name = "Петя"
first_speed = int(input())
second_name = "Вася"
second_speed = int(input())
third_name = "Толя"
third_speed = int(input())

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

p1 = "I"
p2 = "II"
p3 = "III"

print(f"{first_name:^24}")
print(f"{second_name:^8}")
print(" " * 16, f"{third_name:^8}", sep="")
print(f"{p2:^8}", end="")
print(f"{p1:^8}", end="")
print(f"{p3:^8}")
