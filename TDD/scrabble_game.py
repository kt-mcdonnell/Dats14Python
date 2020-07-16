import random


class Game:

    def __init__(self):
        self.score_dict = {1:{'a': 1,    'b': 3,    'c': 3,    'd': 2,
                            'e': 1,    'f': 4,    'g': 2,    'h': 4,    'i': 1,
                            'j': 8,    'k': 5,    'l': 1,    'm': 3,    'n': 1,
                            'o': 1,    'p': 3,    'q': 10,    'r': 1,    's': 1,
                            't': 1,    'u': 1,    'v': 4,    'w': 4,    'x': 8,
                            'y': 4,    'z': 10}}
        self.tile_bag = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.rand_letters = []

    def letter_score(self, letter):
        for key in self.score_dict:
            return self.score_dict[1][letter]

    def get_letters(self):
        for i in range(0,7):
            rand_letters_choice = random.choice(self.tile_bag)
            self.rand_letters.append(rand_letters_choice)
        print("Your letters are: {}".format(self.rand_letters))

    def word_score(self, word):
        total = 0
        for x in word:
            self.score_dict(x)
            total = total + self.score_dict[x]
        return total

    def word_play(self, total):
        your_word = input("Your word: /n")  
        for i in your_word:
            if i in self.rand_letters:
                print("Good work! You scored {}".format(total))
        print(scrabble_score(your_word))


game = Game()
game.get_letters()
print(game.word())
