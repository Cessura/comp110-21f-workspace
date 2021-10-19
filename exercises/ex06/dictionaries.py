"""Practice with dictionaries."""

__author__ = "730330727"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    inverted: dict[str, str] = {}
    errorCheck: int = int(0)
    keys: list[str] = []
    entries: list[str] = []
    i = 0
    
    for index in a:
        for index2 in a:
            if a[index2] == a[index]:
                errorCheck += 1
                if errorCheck > 1:
                    raise KeyError
        errorCheck = 0    

    for key in a:
        entries.append(key)

    for entry in a:
        keys.append(a[entry])

    while i < len(a):
        inverted[keys[i]] = entries[i]
        i += 1

    return inverted


def favorite_color(a: dict[str, str]) -> str:
    """Finds the most identified entry value."""
    workhorse: dict[str, int] = {}
    number: list[int] = []
    color: list[str] = []
    i = 0

    if len(a) < 1:
        raise IndexError

    for value in a:
        if a[value] in workhorse:
            workhorse[a[value]] += 1
        else:
            workhorse[a[value]] = 0

    for i in workhorse:
        number.append(workhorse[i])
        color.append(i)

    while len(number) > 1:
        if number[0] >= number[1]:
            number.pop(1)
            color.pop(1)
        else:
            number.pop(0)
            color.pop(0)

    return color[0]


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a thing occurs in the list."""
    workhorse: dict[str, int] = {}
    comparator: str = str("")
    i = 0

    if len(a) < 1:
        raise IndexError

    while i < len(a):
        workhorse[a[i]] = 0
        i += 1

    i = 0

    while i < len(a):
        for key in workhorse: 
            comparator = key
            if a[i] == comparator:
                workhorse[a[i]] += 1
        i = i + 1 

    return workhorse
