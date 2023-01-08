import random

class BagKegs:
    def __init__(self, count=1):
        self.__keg = list(range(1, 91))

    # метод отдает намер боченка
    @property
    def get_keg(self, count=1):
        if len(self.__keg) and count == 1:
            #удаляю из сумке номер который уже выпал
            value = self.__keg[random.randint(0, len(self.__keg) -1)]
            self.__keg.remove(value)
            count = 0

            return value
        else:
            return "Сумка пуста"

    @property
    def lets_see_bag(self):

        return len(self.__keg)





