import random


SYMBOLS = """
-----------
|    |    |
|    O    |
|   /|\   |
|  / | \  |
|   / \   |
|  /   \  |
|         |
"""

PHASES = [
    0,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
    1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 0,
    1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 2, 0,
    1, 0, 0, 0, 7, 6, 8, 0, 0, 0, 2, 0,
    1, 0, 0, 7, 0, 6, 0, 8, 0, 0, 2, 0,
    1, 0, 0, 0, 9, 0, 10, 0, 0, 0, 2, 0,
    1, 0, 0, 9, 0, 0, 0, 10, 0, 0, 2, 0,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
]


class Game:
    def __init__(self, word):
        word = word.upper()
        self.word = word
        self.initially_open_letters = [word[0], word[-1]]
        self.guessed_letters = []

    def is_letter_open(self, letter):
        return letter in self.initially_open_letters or letter in self.guessed_letters

    def get_obfuscated_word(self):
        letters = [(letter if self.is_letter_open(letter) else '_') for letter in self.word]
        return ' '.join(letters)

    def get_number_of_failures(self):
        return len([letter for letter in self.guessed_letters if letter not in self.word])

    def get_picture(self):
        n = self.get_number_of_failures()
        symbols = [(symbol if phase <= n else ' ') for symbol, phase in zip(SYMBOLS, PHASES)]
        return ''.join(symbols)

    def guess(self):
        obfuscated_word = self.get_obfuscated_word()
        if '_' not in obfuscated_word:
            # The word is completely revealed.
            return True
        print(obfuscated_word)
        letter = input('Guess a letter: ').upper()
        self.guessed_letters.append(letter)
        if letter not in self.word:
            print(self.get_picture())

    def play(self):
        while self.get_number_of_failures() < 10:
            if self.guess():
                print('You win!')
                break
        else:
            print('You are hung!')


with open('words.txt') as f:
    words = [word.strip() for word in f.readlines()]

while True:
    new_game = Game(random.choice(words))
    new_game.play()
    if input('Play again? (Y/N)').upper() != 'Y':
        break
