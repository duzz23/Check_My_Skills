import random
from random import randrange


#Баченок отдает случайные числа от 1 до 90
class Barrel:
    def __init__(self, point=randrange(1,90)):
        self.point = point

    def __str__(self):
        return f'Новый бочонок: {self.point}'


class Plyer:
    def __init__(self, username: str):
        self.username = username

    def __str__(self):
        return f"{self.username}"

player_1 = Plyer('человек')
player_2 = Plyer("robot")


# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны
class Card:

    line1 = random.sample((range(1, 91)), 9)
    line2 = random.sample((range(1, 91)), 9)
    line3 = random.sample((range(1, 91)), 9)

    def __int__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3

    def __str__(self):
        return f'------ карточка {player_1}  -----\n{self.line1}\n{self.line2}\n{self.line3}'




card = Card()

barrel = Barrel()


class Game:


    def __int__(self, card, barrel, player_1, player_2):
        self.card = card
        self.barrel = barrel
        self.player_1 = player_1
        self.player_2 = player_2

    def __str__(self):
        return f'{barrel}\n{player_1} and {player_2}\n{card}'


    for cv in card.line1:
        if cv == barrel.point:
            cv = '-'
            print('в 1 линии есть')
    for cv2 in card.line2:
        if cv2 == barrel.point:
            cv2 = '-'
            print('в 2 линии есть')

    for cv3 in card.line3:
        if cv3 == barrel.point:
            cv3 = '-'
            print('в 3 линии есть')
print(Game())

