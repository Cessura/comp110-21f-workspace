"""Finding duplicate letters in a word."""

__author__ = "730330727"

comparator: str = str("")
considered: str = str("")
i: int = int(0)
n: int = int(0)
result: str = str("False")
phrase: str = str(input("Enter a word: "))

while i < len(phrase):
    comparator = phrase[i]

    while n < len(phrase):
        if i == n:
            n = n + 1

        if n < len(phrase):
            considered = phrase[n]

        if considered == comparator:
            result = "True"
        n = n + 1

    i = i + 1
    n = 0

print("Found duplicate: " + result)