"""
file: wordData.py
language: python3
author: Aakash Jaideva
purpose: takes text file and turns it into a dictionary of dictionaries
"""


def readWordFile(fileName):
    """
    reads data file and creates dictionaries mapping words
    :param fileName: A string
    :return: A dictionary
    """
    words_dict = {}
    current_word = None
    actual_name = 'data/' + fileName

    with open(actual_name) as file:
        for line in file:
            line = line.strip()
            if ',' not in line:
                current_word = line
                words_dict[current_word] = {}
            else:
                year, count = [int(x) for x in line.split(',')]
                words_dict[current_word][year] = count

    return words_dict


def totalOccurrences(word, words):
    """

    :param word: word to calculate count
    :param words: A dictionary
    :return: Total times word appears
    """
    total = 0
    if word in words:
        for year in words[word]:
            total += words[word][year]
    return total


def main():
    """
    takes input
    """
    print((totalOccurrences(input('Enter word '), readWordFile(input('Enter filename ')))))


if __name__ == '__main__':
    main()
