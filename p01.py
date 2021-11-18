"""
Puzzle 01:

Given a word, reverse the word.
Given a sentence, reverse the words in the sentence.
"""


def reverse(text):
    words = text.split(" ")

    if len(words) == 1:
        return words[0][::-1]

    return " ".join(words[::-1])


if __name__ == "__main__":

    print(reverse("word"))
    print(reverse("this is a sentence"))
