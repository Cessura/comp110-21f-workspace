"""Counting letters in a string."""

__author__ = "730330727"


# Begin your solution here...

letter: str = str(input("What letter do you want to seach for?: "))
word: str = str(input("Enter a word: "))
i: int = int(len(word))
score: int = int(0)

while i > 0:
    if letter == word[i - 1]:
        score = score + 1
    i = i - 1

print("Count: " + str(score))
