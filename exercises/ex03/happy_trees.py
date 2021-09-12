"""Drawing forests in a loop."""

__author__ = "730330727"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int (input("depth: "))
sapling: str = str (TREE)
i: int = int(0)

if depth > 0 :
	while  i < depth:
		print (sapling)
		sapling = sapling + TREE
		i = i + 1
else: 
    print("deforestation...")