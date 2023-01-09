from pytest import fixture, mark, param
from Lotto_Geme.card import Card
from Lotto_Geme.keg import BagKegs


class TestBagKegs:

    def test_get_keg(self):
        result = BagKegs().get_keg
        assert result > int(0)

    def test_lets_see_bag(self):
        result = BagKegs().lets_see_bag
        assert result == 90


@fixture
def card_instance() -> Card:
    return Card("Andrey")




class TestCard:

    def test_if_copm_tap_n2(self, card_instance, value='n'):
        result = card_instance.if_copm_tap_n(value)
        assert result == True


    # Данный тест нужно доработат, не понял как сделать проверку "if str(value) in self.__matrix:"
    # def test_if_copm_tap_y(self, value="y"):
    #     Card("Andrey").self.__matrix = ['y']
    #     result = Card("Andrey").if_copm_tap_y(value)
    #     assert result == True