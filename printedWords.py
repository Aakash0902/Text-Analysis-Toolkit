"""
file: printedWords.py
language: python3
author: Aakash Jaideva
purpose: counts number of words
"""

import wordData
import matplotlib.pyplot as plt


def printedWords(words):
    years = set()
    for word in words.values():
        years.update(word.keys())
    sorted_years = sorted(years)
    result = []
    for year in sorted_years:
        total_count = sum(word_data.get(year, 0) for word_data in words.values())
        result.append((year, total_count))
    return result




def wordsForYear(year, yearList):
    for entry in yearList:

        if entry[0] == int(year):

            return entry[1]
    return 0



def main():
    file_name = input('Enter file name: ')
    year_input = input('Enter year: ')
    word_data = wordData.readWordFile(file_name)

    total_words_for_year = wordsForYear(year_input, printedWords(word_data))
    print("Total printed words: " + str(total_words_for_year))

    years = []
    count = []
    for entry in printedWords(word_data):
        years.append(entry[0])
        count.append(entry[1])
    plt.plot(years, count)
    plt.show()


if __name__ == '__main__':
    main()


