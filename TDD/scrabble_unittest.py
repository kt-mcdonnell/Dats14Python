from scrabble_game import Game()
from random import choice

my_game = Game()


def test_letter_score():
    assert my_game.letter_score('a') == 1
    assert my_game.letter_score('g') == 2
    assert my_game.letter_score('c') == 3
    assert my_game.letter_score('v') == 4
    assert my_game.letter_score('k') == 5
    assert my_game.letter_score('j') == 8
    assert my_game.letter_score('z') == 10

def test_get_letters():
    assert my_game.get_letters() == 7

def test_score_calc():
    assert my_game.score_calc("peach") == 11
    assert my_game.score_calc("zebra") == 16
    assert my_game.score_calc("quick") == 20
    assert my_game.score_calc("toaster") == 7
    assert my_game.score_calc("eat") == 3