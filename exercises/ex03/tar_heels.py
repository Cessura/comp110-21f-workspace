"""An exercise in remainders and boolean logic."""

__author__ = "730330727"


# Begin your solution here...
    
raci: str = str("CAROLINA")
num: int = int(input("Enter an int: "))

if num % 2 == 0: 
    raci = "TAR"

if num % 7 == 0:
    raci = "HEEL"

if num % 14 == 0:
    raci = "TAR HEEL"

print(raci)