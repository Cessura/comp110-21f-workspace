"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730330727"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

det: int = int(randint(1, 5))

print("Your fortune cookie says...")
if det == 1:
    print("\"The last time I heard that truth, I found a trator in every trusted face. That truth will soon be yours; You must prepare.\"")
else:
    if det == 2:
        print("\"Ennie meenie minie moe, catch a tiger by the toe. if it hollars, you have a real tiger. Please release it or you might die\"")
    else:
        if det == 3:
            print("\"A vibe. good? bad? idk. Sure is a vibe tho. Good luck\"")
        else:
            if det == 4:
                print("\"I've heard you like being alive, right? Take 1 step to your right in exactly 19,903 seconds, or who knows what unfortunate, unpleseant, unsavory things could happen to people you love. :)\"")
            else:
                if det == 5:
                    print("\"Gottem\"")
print("Now, go spread positive vibes!")