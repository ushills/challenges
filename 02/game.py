#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH

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


def max_word_value(wordlist=data.load_words()):
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



def main():
    pass


if __name__ == "__main__":
    main()
