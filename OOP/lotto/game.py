from card import Card
import random
import time
from keg import BagKegs

def game():

    user = Card((input('         ***Начнем игру***\n'
                       'Напиши свое имя: ')))
    comp = Card('Робокоп')
    time.sleep(1)
    user.show_card()
    print("Это твоя карточка на эту игру, можешь ее не запоминать, она будет демонстрироваться каждый ход")
    time.sleep(6)
    print('\nКраткие правила:\nКомпьютер достает первый бочонок с номером!\n'
          'Eсли на твоей карточке есть клетка с номером выпавшего бочонка,\n'
          'то ты должен нажать "Y", если нет, в таком случае нажимай "N"')
    time.sleep(9)
    print('ГОТОВЬСЯ')
    time.sleep(1)
    print('   3')
    time.sleep(1)
    print('   2')
    time.sleep(1)
    print('   1')
    print('\nStart game\n')
    bag = BagKegs()
    for i in range(1, 91):
        if user.find_num == True and comp.find_num == True:
            toss = 1
            while toss == 1:
                time.sleep(1)
                print('------------------------------------------------------------------------------------')
                print('Трясем мешок')
                time.sleep(2)
                x = bag.get_keg
                print(f'Вытаскиваем бочонок номер {x}\n')
                time.sleep(3)
                comp.show_card()
                user.show_card()
                time.sleep(3)
                print('Компуктер, есть ли у тебя такая цифра или нет?(Y or N)')
                time.sleep(3)
                comp_chance = random.randint(0, 1001)
                if comp_chance < 999: #даем возможность компьютеру ошибиться
                    if str(x) in comp._return_matrx():
                        comp_input = 'Y'
                        print(comp_input)
                    else:
                        comp_input = 'N'
                        print(comp_input)
                else:
                    if str(x) in comp._return_matrx():
                        comp_input = 'N'
                        print(comp_input)
                    else:
                        comp_input = 'Y'
                        print(comp_input)
                if comp_input == 'Y':
                    comp.if_copm_tap_y(x)
                    if comp.find_num == True:
                        time.sleep(2)
                        toss = 2
                elif comp_input == 'N':
                    comp.if_copm_tap_n(x)
                    toss = 2
                coun = 1 # для того чтобы если пользователь ошибся, алгорим ввода запустился заново
                while coun == 1:
                    user_input = input(f'\n{user.name}, есть ли у тебя такая цифра??(Y or N)' )
                    if user_input == 'y' or user_input == 'Y':
                        user.if_tap_y(x)
                        if user.find_num == True:
                            time.sleep(3)
                            # print('Хорошо!')
                            toss = 2
                            coun = 2
                    elif user_input == 'n' or user_input == 'N':
                        user.if_tap_n(x)
                        toss = 2
                        coun =2
                    else:
                        print('Вероятно вы ошиблись! Вы должны ответить да(Y), либо нет(N)')
                print(f'количество оставшихся бочонков: {bag.lets_see_bag} \n')
                time.sleep(2)
                print('------------------------------------------------------------------------------------')
        elif user.find_num == False:
            print(f'{user} win')
            raise SystemExit
        elif user.find_num == False and comp.find_num == False:
            print('ничья')
            raise SystemExit
        else:
            print('compucter win')
            raise SystemExit


game()