import pytest
from ClassDobbleGame import DobbleGame

class TestDobbleGame:
    def setup_method(self):
        self.game = DobbleGame(5)

    def test_generate_cards(self):
        assert len(self.game.cards) == 6

    def test_play(self):
        pass