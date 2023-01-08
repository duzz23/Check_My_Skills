import random
import time


class Card:
    def __init__(self, name):
        self.name = name
        self.__matrix = []
        self.c = False

    """ __make_card() создаем карту (пример)
    [' ', 55, 23, ' ', 87, 19, 84, ' ', ' ']
    [83, 41, ' ', 81, 38, ' ', 18, ' ', ' ']
    [77, ' ', ' ', ' ', 82, ' ', 11, 39, 21]
    """
    def __make_card(self):
        while not self.c:
            user_card = []
            list_of_nums = list(range(1, 90))  # список чисел которым заполняется карточка
            count = 1
            # Создаем три строчки
            for i in range(3):
                matx = []
                # Наполняем 6 случайними цифрами в строчке
                for i in range(6):
                    counter = random.randint(0, len(list_of_nums) - 1)
                    num = list_of_nums[counter]
                    matx.append(num)
                    # удаляем числа из списка которые уже выбрали
                    list_of_nums.remove(num)
                # Наполняем 3 пробелами в строчке
                for i in range(3):
                    matx.append(' ')
                #shuffle() перемешиваем числа и пустые строки в словаре
                random.shuffle(matx)
                # заполняем 9 ячейек случайным набором и добавляем в карточку
                for i in range(9):
                    user_card.append(str(matx[i]))
            self.__matrix = user_card
            self.c = True

    def show_card(self):
        self.__make_card()
        print(f'Карточка игрока {self.name}')
        print('------------------------')
        print(' '.join(self.__matrix[:9]))
        print(' '.join(self.__matrix[9:18]))
        print(' '.join(self.__matrix[18:28]))
        print('------------------------\n')

    # возврат списка номеров карточки
    def _return_matrx(self):
        self.__make_card()
        return self.__matrix

    # проверим наличие чисел в карточке игрока
    @property
    def find_num(self):
        self.num_count = 0
        self_matx = self._return_matrx()
        for i in range(len(self_matx)):
            try:
                # num = int(self_matx[i])
                self.num_count += 1
            except ValueError:
                pass
        if self.num_count > 0:
            return True
        elif self.num_count < 0:
            return False

    def if_tap_y(self, value):
        if str(value) in self.__matrix:
            #insert() заменяем число на "-"
            self.__matrix.insert(self.__matrix.index(str(value)), ' - ')
            # remove() удаляем выпавшое число из списка, что бы не выпало повторно
            self.__matrix.remove(str(value))
            print('Верно! Идем дальше!')

            return True
        else:
            print("Ошибка, такого числа у тебя на карточке нет!\nТы проиграл")
            time.sleep(3)
            print('пока')
            raise SystemExit

    def if_copm_tap_y(self, value):
        if str(value) in self.__matrix:
            # insert() заменяем число на "-"
            self.__matrix.insert(self.__matrix.index(str(value)), ' - ')
            # remove() удаляем выпавшое число из списка, что бы не выпало повторно
            self.__matrix.remove(str(value))
            print('Компуктер прав! Идем дальше!')

            return True
        else:
            print("Компуктер ошибся, ты победил")
            time.sleep(6)
            print('пока')
            raise SystemExit

    def if_copm_tap_n(self, value):
        if str(value) in self.__matrix:
            print("Компуктер ошибся, ты победил")
            time.sleep(6)
            print('пока')
            raise SystemExit
        else:
            print("Верно! Идем дальше!")
            return True

    def if_tap_n(self, value):
        if str(value) in self.__matrix:
            print("Ты совершил ошибку, это число у тебя есть!\nТы проиграл")
            time.sleep(3)
            print('пока')
            raise SystemExit
        else:
            print("Верно! Идем дальше!\n")
            return True


