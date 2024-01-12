"""
file: letterFreq.py
language: python3
author: Aakash Jaideva
purpose: compares frequency
"""


import wordData
import matplotlib.pyplot as plt


def letterFreq(words):
    """
    plots frequency of letters
    :param words: dictionary
    :return: A string
    """
    letter = {}
    for word, year_data in words.items():
        for year, count in year_data.items():
            for char in word:
                if char in letter:
                    letter[char] += count
                else:
                    letter[char] = count
    dict = letter
    sorted_letters = sorted(letter.keys(), key=lambda x: letter[x], reverse=True)
    result_string = ''.join(sorted_letters)
    plt.bar(list(sorted(dict.keys())), list(dict.values()), color='skyblue')
    plt.show()
    return result_string


def main():
    """
    takes user input
    """
    print("Letters sorted by decreasing frequency: " + letterFreq(wordData.readWordFile(input("Input file name "))))



if __name__ == '__main__':
    main()

