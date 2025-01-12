"""List utility functions part 2."""

__author__ = "123456789"

# Define your functions below

"""List utility functions."""

__author__ = "730330727"


# TODO: Implement your functions here.

def only_evens(A: list[int]) -> list[int]:
    """Gives only even numbers."""
    B: list = []
    i: int = int(0)

    while i < len(A):
        B.append(A[i])
        i += 1

    i = 0

    while i < len(B):
        if B[i] % 2 != 0:
            B.pop(i)
        else: 
            i += 1
        
    return B


def sub(A: list[int], i: int, j: int) -> list[int]:
    """Makes a subset list."""
    C: list[int] = []

    if i < 0:
        i = 0

    if i > j:
        return C

    if j <= 0:
        return C

    if len(A) == 0:
        return C

    if j > len(A):
        j = len(A)

    while i < j:
        C.append(A[i])
        i += 1

    return C


def concat(A: list[int], B: list[int]) -> list[int]:
    """Pulls two lists together."""
    C: list[int] = []
    i: int = int(0)

    while i < len(A):
        C.append(A[i])
        i += 1

    i = 0

    while i < len(B):
        C.append(B[i])
        i += 1

    return C