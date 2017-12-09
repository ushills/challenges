#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from random import randint

NUM_LETTERS = 7


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = word.upper()
    score = 0
    for letter in word:
        # print(letter)
        score += LETTER_SCORES[letter]
    # print('The score for the word', word, 'is', score)
    return score


def max_word_value(wordlist=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    max_score = int()
    for word in wordlist:
        word = re.sub('[^a-zA-Z]+', '', word)
        try:
            score = calc_word_value(word)
            if score > max_score:
                max_score = score
                max_word = word
        except KeyError as e:
            print('KeyError', e, word)
    return max_word


def draw_letters():
    """ Draw a number of letters (NUM_LETTERS) from the POUCH
    as the POUCH is a list you need to select a random letter
    (NUM_LETTERS) times"""
    return [POUCH[randint(0, 98)] for i in range(NUM_LETTERS)]


def main():
    letters = draw_letters()
    print(letters)
    pass


if __name__ == "__main__":
    main()
