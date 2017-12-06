from data import DICTIONARY, LETTER_SCORES
import re


def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY) as fhand:
        for word in fhand:
            word = word.strip()
            # print(word)
            words.append(word)
    # print('Found', len(words), 'words')
    return words


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


def max_word_value(wordlist=load_words()):
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


if __name__ == "__main__":
    wordlist = load_words()
    max_word = max_word_value(wordlist)
    print(max_word)
