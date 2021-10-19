"""examples of afunction that processes a list."""

#define a function named contains 
#we can give two arguments: a needle value we're searching for in a haystack list

def main() -> None:
    names: list[str] = ["kris", "kaki"]
    print(containts("kris",names))

    
def containts(needle:str, haystack: list[str]) -> bool:
    """return true if needle is found in haystack, false otherwise"""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False

if __name__ == "__main__":
    main()