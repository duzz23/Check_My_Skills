"""Генераторы"""
# генераторы это функции которая отличается отдает значения и контроль над тем местом откуда отдал
# Передача контроля из функции генератора и обратно
# проше говоря отдает элимент останавливается при повторном обрашение отдает следующий элимент и дак далее
# функция next() сдвигает выполнение команды до след yield

from time import time

#
# def gen(s):
#     for i in s:
#         yield i
#
# g = gen('oleg')

# python3 -i 3_generators.py
# next(g)

# Простаю функция Генерирует имена для фаилов

def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000) #сделали счетчик в мили секундах
        yield pattern.format(str(t))

# Генераторы выполняются по очереди и мы получим // o 0 l 1 e 2 g 3
def gen1(n):
    for i in n:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('Oleg')
g2 = gen2(4)

# ОЧередь задач
tasks = [g1, g2]
# wbrk

while tasks:
    task = tasks.pop(0) #pop - перемешает и удаляет из списка

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
       pass

#python3 -i 3_generators.py
