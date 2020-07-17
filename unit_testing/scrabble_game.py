import random


class Game:

    def __init__(self):
        self.score_dict ={'a': 1,    'b': 3,    'c': 3,    'd': 2,
                            'e': 1,    'f': 4,    'g': 2,    'h': 4,    'i': 1,
                            'j': 8,    'k': 5,    'l': 1,    'm': 3,    'n': 1,
                            'o': 1,    'p': 3,    'q': 10,    'r': 1,    's': 1,
                            't': 1,    'u': 1,    'v': 4,    'w': 4,    'x': 8,
                            'y': 4,    'z': 10}
        self.rand_letters = []

    def letter_score(self, letter):
        for letter in self.score_dict:
            return self.score_dict.keys

    def get_letters(self):
        for i in range(0,7):
            rand_letters_choice = random.choice(self.score_dict.keys)
            self.rand_letters.append(rand_letters_choice)
        print("Your letters are: {}".format(self.rand_letters))

    def word_score(self, letter, your_word):
        total = 0
        for letter in your_word:
            self.letter_score(letter)
            total = total + self.letter_score[letter]
        return total

    def word_play(self, total):
        your_word = input("Your word: /n")  
        for i in your_word(i):
            if i in self.rand_letters:
                print("Good work! You scored {}".format(total))
        print(word_score(your_word))


game = Game()
game.get_letters()
print(game.word_play())
