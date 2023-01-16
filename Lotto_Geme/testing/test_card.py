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
    card = Card("Andrey")
    card._Card__matrix = [
    '4', '39', ' ', '52', '37', '13', '46', ' ', ' ',
    ' ', '12', '79', ' ', '11', '73', '45', ' ', '51',
    '55', ' ', '83', '30', '14', ' ', ' ', '16', '88'
    ]
    return card

class TestCard:

    def test_if_copm_tap_y(self, card_instance):
        result = card_instance.if_copm_tap_y('4')
        assert result is True

    def test_if_copm_tap_n2(self, card_instance):
        result = card_instance.if_copm_tap_n('5')
        assert result is True
