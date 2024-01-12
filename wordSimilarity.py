"""
file: wordSimilarity.py
language: python3
author: Aakash Jaideva
purpose: prints words similar to given word
"""

import math

import wordData


def get_words(dict, val):
    keys = ''
    for key, value in dict.items():
        if value == val:
            keys += key
    return keys


def topSimilar(words, target_word):

    word_Data = {}

    for word in words:
        year_data = words[word]
        year_counts = []
        sum_squares = 0

        for occur in words[word]:
            sum_squares += words[word][occur] ** 2

        sqrt = math.sqrt(sum_squares)

        for i in words[word]:
            words[word][i] = float(words[word][i] / sqrt)

        for year in year_data:
            year_counts.append(words[word][year])

        word_Data[word] = year_counts

    if target_word not in word_Data:
        return [target_word]

    target_vect = word_Data[target_word]
    similarity = {}

    for new_words in word_Data:
        compare_vect = word_Data[new_words]
        dot_prod = sum(x * y for x, y in zip(target_vect, compare_vect))
        similarity[new_words] = dot_prod

    sorted_similarity = sorted(similarity.values())[::-1]
    if len(sorted_similarity) > 5:
        sorted_similarity = sorted_similarity[0:5]

    final_words = []
    for item in sorted_similarity:
        final_words.append(get_words(similarity,item))

    return final_words


def main():
    print(topSimilar(wordData.readWordFile(input('Enter filename: ')), input('Enter word: ')))


if __name__ == '__main__':
    main()






