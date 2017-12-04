from data import DICTIONARY, LETTER_SCORES


def load_words():
    words = []
    fhand = open(DICTIONARY)
    for word in fhand:
        word = word.strip()
        # print(word)
        words.append(word)
    print('Found', len(words), 'words')
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = word.upper()
    score = None
    for letter in word:
        print(letter)
        LETTER_SCORES(letter)
    print('The score for the word', word, 'is', score)
    pass


def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass


if __name__ == "__main__":
    load_words()
    calc_word_value('test')
    pass # run unittests to validate
