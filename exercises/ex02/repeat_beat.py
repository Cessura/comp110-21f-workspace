"""Repeating a beat in a loop."""

__author__ = "730330727"


# Begin your solution here...

beat: str = str("")
unit: str = str(input("What beat do you want to repeat? "))
count: int = int(input("How many times do you want to repeat it? "))
i: int = 0

if count > 0:
    i = count - 1
    while i > 0:
        beat = unit + " " + beat
        i = i - 1
    else:
        print(beat + unit)

else:
    print("No beat...")