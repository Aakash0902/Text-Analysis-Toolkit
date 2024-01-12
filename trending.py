"""
file: trending.py
language: python3
author: Aakash Jaideva
purpose: prints top trending words
"""


import wordData


def trending(words, start, end):
    """
    returns top trending words
    :param words: Dictionary
    :param start: Start Year
    :param end:  End Year
    :return: list
    """
    result = []
    for word, counts in words.items():
        if start in counts and end in counts:
            if counts[start] >= 1000 and counts[end] >= 1000:
                trend_value = counts[end] / counts[start]
                result.append((word, trend_value))
    result.sort(key=lambda x: x[1], reverse=True)
    return result


def main():
    """
    user input
    :return: string
    """
    words = wordData.readWordFile(input("Enter filename: "))
    start = int(input("Enter start year: "))
    end = int(input("Enter end year: "))
    r_list = trending(words, start, end)
    top_words = [word for word, trend in r_list]
    print("\nThe top trending words:")
    for word in top_words[:10]:
        print(word)


if __name__ == '__main__':
    main()
