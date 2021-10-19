A: list[int] = [10, 20, 30, 40]
B: list[int] = [20, 30, 40, 50, 60, 70, 1]


def only_Evans(A: list[int]) -> list[int]:
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