from random import randrange


class Barrel:
    def __init__(self, point: int):
        point <= 90
        #Всего 90 бочонков с цифрами от 1 до 90 (В жизни они обычно достаются из мешка чтобы можно было вытянуть случайно)
        self.point = point

    def __str__(self):
        return self.point


# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны
class Cards:
    def __init__(self, card_number: int):
        self.card_number = card_number

    def __str__(self):
        return self.card_number


class Plyer:
    def __init__(self, username: str, count: int):
        self.username = username
        self.count = count

    def __str__(self):
        return f"{self.username} {self.count}"


class Lottery:
    ticket = Cards()
    plyer = Plyer()


numbers = randrange(1,90)
