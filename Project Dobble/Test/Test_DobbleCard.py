import pytest
from Dobble import DobbleCard

class TestDobbleCard:
    def setup_method(self):
        self.card = DobbleCard(['Яблоко', 'Банан', 'Вишня', 'Собака', 'Слон', 'Лягушка', 'Гитара', 'Сердце', 'Мороженое', 'Лось', 'Ключ', 'Лимон'])

    def test_repr(self):
        expected = "DobbleCard(['Яблоко', 'Банан', 'Вишня', 'Собака', 'Слон', 'Лягушка', 'Гитара', 'Сердце', 'Мороженое', 'Лось', 'Ключ', 'Лимон'])"
        assert repr(self.card) == expected

    def test_symbols(self):
        assert self.card.symbols == ['Яблоко', 'Банан', 'Вишня', 'Собака', 'Слон', 'Лягушка', 'Гитара', 'Сердце', 'Мороженое', 'Лось', 'Ключ', 'Лимон']