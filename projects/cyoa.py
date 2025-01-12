"""A CYOA Game."""

__author__ = "730330727"

from random import randint
# used in drawGarden()

# submission requirements and main() variables
player: str = str("")
points: int = int(0)
WAVE_EMJOI: str = str("\U0001F44B")
disablePoints: bool = False
minutes: int = int(180)

# garden visualizers
plants: str = str("")
patterns: str = str("")
flower1: str = str("")
flower2: str = str("")
flower3: str = str("")
flower4: str = str("")

# flow managers
location: int = int(0)
SearchLoc: int = int(0)
Choice1: str = str("")
Choice2: str = str("")
Choice3: str = str("")
FloPlus: int = int(0)

# scene descirptions
SurDesc: str = str("You stand on a bank of silvery, mist-fine sand, one of the many that stretch out behind you all the way to the horizon. Without the light of the sun or moon to blind you, the rich, inky-blue skies shine brighter than you could have ever imagined by light of only stars, as if this place had always been their home, or the stage on which they’ve always loved to perform. Other places you’ve been have been spaces you stood on, or arrived at; but here, you feel certain this is a place you were placed within, between the sky and its banks. You wonder what flower you might find here.")
AloDesc: str = str("Vibrant leaves bursting ruby and amber fill a canopy that stretches across the entire vista. Sharp cliffs jut out from the sea of sunset colors, revealing blocks of gleaming, gypsum white geometries. As if part of a match set, you examine the trees closest from where you stand and see they are covered in birch white bark. You don’t see any animals, or traces thereof- but standing here, with your back to a literal shore and your eyes taking in this metaphorical one, you still feel this place is a glittering treasure of life. You wonder what flower you might find here.")
EveDesc: str = str("For a moment, a beam of sunlight seems to blind you, but you realize that what lays before you is just relatively dim. You’re standing on wood, and further look around reveals its the massive branch of a Yggdrasil sized tree, only one of many in this forest of absurd scale. More sunbeams spill down from the canopies above- of which it seems there are many. Tiny motes of light drift toward and away from you, a few landing on your outstretched hand before lifting away. A sense of childlike wonder washes over you; you wonder what flower you might find here.")
YunDesc: str = str("You look up and a new kind of island looms before you: a massive cluster of slate-like stone pinned in the sky, draped in long, thick vines and topped with emerald fields of grass. Many similar islands hang in the sky around you, each of them cloaked in part by fluffy clouds catching the sun’s rays. You look below you and see that you are also on one of these sky islands- and the thick vines spilling over the edge seem to connect the islands in a great web, with one leading straight to your feet. You wonder what flower you might find here.")
MemDescSur: str = str("A memory of the stars blurred by ripples")
MemDescAlo: str = str("A memory of leaves drifting in autumn")
MemDescEve: str = str("A memory of climbing a tree, many years ago")
MemDescYun: str = str("A memory of rolling hills")

# in-flow scene descriptions
SearchResAlo1: str = str("As you make your way to the nearest looming cliff, you find that no matter how far you walk, the cliff near seems to get closer. As scarlet leaves drift around you, you lean on a nearby tree to catch your breath; once you’ve recovered, you let your eyes close and take one long, deep breath of appreciation before pushing on. When you open your eyes, you find you’re on the top of the cliff- with a beautiful flower in front of you.")
SearchResAlo2: str = str("You walk along the shore, deciding not to disturb the beautiful bounty of nature by entering. You watch the waves role in from the clear horizon and at the forests edge, and find moments of inspiration.")
SearchResAlo3: str = str("You walk into the forest floor, no end goal in mind. An untold amount of time passes while you wander between the trunks, glancing at the spectacle around you.")
SearchResYun1: str = str("Seeing this impossible sight reminds you of the nature of this reality, and you’re freed from any fear or reservations about danger. Throwing caution to the wind, you run and leap off of the island, skydiving towards the nearest landmass. As you fall, the islands move around you in the distant sky, forming the image of a symmetrical flower. Once you land on your feet without any kind of injury, your mind fills in the colors and the image is perfectly captured in your head.")
SearchResYun2: str = str("You begin walking the dubious web of vines, seeing a wide stretch of the islands before you. You notice not every island is connected in this natural web however, and it give you a moment of inspiration as you see each new vista.")
SearchResYun3: str = str("You decide to scour the grass around your ankles for a flower worthy of your garden, focused on the task at hand as opposed to the gorgeous vista. Your search turns up short; plenty of short plant life, but no flower. The search did yield a moment of inspiration however.")
SearchResEve1: str = str("You try to climb to the upper canopy. As you climb, you find that you don’t get tired, and the glowing motes swirl around with curiosity, or maybe encouragement. However, by the time you make it to the next canopy up, you see the top is no closer. Along the way you found moments of inspiration.")
SearchResEve2: str = str("You decide to try to climb down the trunk. As you start, the glowing motes swirl around you; suddenly, on your next step, you find you’ve stepped into a glowing mat of their construction. They gently drift to the ground, and you step off on the forest floor. Before you lies a flower, highlighted by a rare sunbeam.")
SearchResEve3: str = str("You walk along the branches around you and find their twisting, spiraling pitches and rises delightful. Each split is another choice that will lead to something new; you walk until you’ve had many moments of inspiration.")
SearchResSur1: str = str("You stare at the slowly shifting stars for what seem like days. The constellations make themselves known to you readily; you swear you can ever see faint traces of light connecting the points. They reveal many scenes to you, each of surprising detail; but you only find a moment of inspiration.")
SearchResSur2: str = str("You look down and stare at the glowing waves that echo out from your feet. The foam is surprisingly fine and detailed; and after looking for a long time, appreciating the bioluminescent beauty, a foam pattern forms a perfect image of a flower. Your mind fills in the colors and the image is perfectly captured in your head.")
SearchResSur3: str = str("You walk through the shallow channels formed by the water, sifting through the sands of the various bars as you go. Unfortunately, you don’t find any signs of plant life here, though you did have a moment of inspiration.")
SubLocSur1: str = str("Search the shifting, glittering stars")
SubLocSur2: str = str("Search within the patterns of the glowing waves at your feet")
SubLocSur3: str = str("Search the ever expanding banks of silvery sand")
SubLocAlo1: str = str("A nearby cliff in front of you")
SubLocAlo2: str = str("Along the shore")
SubLocAlo3: str = str("Deeper in the forest floor")
SubLocEve1: str = str("Climb to the upper canopy")
SubLocEve2: str = str("Scale down the trunk and walk along the roots")
SubLocEve3: str = str("Walk along the branches around you")
SubLocYun1: str = str("Try to catch one of the islands far below you")
SubLocYun2: str = str("Climb the vines strung across the sky")
SubLocYun3: str = str("Look closely in the grassy field you stand in")


def main() -> None:
    """The main menu from which the game and other options are launched. Exit option contains the emoji requirement."""
    i = 1

    global points

    greet()
    while i > 0:
        print("Would you like to view instructions, reset your points, or begin a REM cycle and start the game? You can also choose to exit altogether.")
        print("")
        print("1: Instructions")
        print("2: Reset your points")
        print("3: Begin the game")
        print("4: Exit the program")
        mainChoice: int = int(input("Please input the int value of the choice you'd like to select: "))
        if mainChoice == 1:
            instructionsProcedure()
            print("")
        if mainChoice == 2:
            points = resetFunction(points)
            print("")
        if mainChoice == 3:
            runGame()
        if mainChoice == 4:
            print(f"You decide to return to reality, and wake up. {WAVE_EMJOI}")
            print("")
            print(f"Points accumulated: {points}")
            print("")
            drawGarden()
            return None


def greet() -> None:
    """Greets the player."""
    global player

    print("")
    player = input("Hello! What is your name? ")
    print("")
    print(f"Well {player}, you've fallen asleep, and this time, you're dreaming of a game. Welcome to Dream Gardener!")
    print("In this game, the goal is to explore your various dreamscapes to find flowers for your garden and gather points.")


def instructionsProcedure() -> None:
    """The 'Custom Procedure' requirement. Gives instructions on how to run the game.""" 
    global player
    global points
    chosenPattern: int = int(1)

    print("")
    print("The objective of the game is to navigate your changing dreamscape to find flowers to add to a garden. Each new dreamscape will give you inspiration to draw a floral pattern, but if you look in the right places, you may find an actual flower! Once you run out of REM cycles, you'll use your lucid dream to manifest your garden with the flowers and patterns you've found, surrounded by an envionrment influenced by your journeys.")
    print("While time isn't quite 1 to 1 in a dream, knowing what flower you're looking for makes finding it much faster- if you pick the right flower to look for in the dreamscape and successfully find that flower, that exploration won't decrease the amount of turns before you have to wake up!")
    print("If you'd rather leave the space occupied by a flower blank, you can choose to pass on gaining inspiration or commiting a flower to memory.")
    print("")
    print("When selecting options, make sure to use only integer values, or the entire game will crash and you'll loose all of your progress!")
    print("Here's an example.")
    print("")
    print(f"{player} came across a fish.")
    print("")
    print("Catch the fish")
    print("Let the lad be")
    print("")
    print("Enter the number of the option you'd like to choose: 2")
    print("The lad was let be.")
    print("")
    print("You also are able to represent your progress as points, if you prefer a game with an objective of that kind. Commiting a Flower to memory grants 10 points, while patterns grant 3 each. Just remember that you can only commit up to 4 flowers to memory!")
    print("lets show an example of that in action. Pick an option:")

    print(f"Your current points are {points}.")
    print("Choose a pattern: ")
    print("❈")
    print("❁")
    print("፨")

    chosenPattern = (int(input("Enter the number of the choice you'd like to select: ")))
    if chosenPattern == 1:
        points = points + 3
        print(f"You chose ❈. Your current points are {points}.")
    if chosenPattern == 2:
        points = points + 3
        print(f"You chose ❁. Your current points are {points}.")
    if chosenPattern == 3:
        points = points + 3
        print(f"You chose ፨. Your current points are {points}.")
    print("Okay, you're ready to get dreaming now. You'll have to find that pattern in a dreamscape, but we'll let you keep the points!")
    print("Sweet dreams, and welcome to Lucid Gardener!")


def resetFunction(points: int) -> int:
    """The 'Custom Function' requirement. Allows you to reset your points without leaving the game altogether."""
    reset: int = int(2)
    global disablePoints

    print("Would you like to reset your points? You can also disable points displaying.")
    print("")
    print("Reset points")
    print("Don't reset points")
    print("Disable points")
    reset = int(input("Enter the number of the choice you'd like to select: "))
    
    if reset == 1:
        print("you decided to reset your aquired points.")
        points = 0
        print(f"Your total points are: {points}")
        return points
    if reset == 3:
        print(f"You chose to enjoy expereinces for what they're worth, and to subvert the arbitrary. This is the last time you will see points display: {points}")
        disablePoints = True
        return points
    else: 
        print("You decided to keep your sense of accomplishment.")
        print(f"Your total points are: {points}")
        return points


def runGame() -> None:
    """Runs the game, and creates the loop that allows it to be repeated."""
    global plants
    global patterns
    global flower1
    global flower2
    global flower3
    global flower4
    
    while minutes > 0:
        locationSelector()
        fChoice: int = flowerSelector()
        SearchLoc = searchSelector()
        exploreResult(SearchLoc, fChoice)
        if disablePoints is False:
            print(f"Your current point total is {points}.")
            print(f"You estimate you have {minutes} minutes left asleep--enough to see {minutes//90} more dreamscapes.")
        if disablePoints is True:
            if minutes > 0:
                print("You think about the expereinces you've had so far, and try to imagine what your garden might look like.")
                print(f"You estimate you have {minutes} minutes left asleep--enough to see {minutes//90} more dreamscapes.")
                drawGarden()
    print("You get the overwhelming feeling that you will wake up soon. As the minutes run out, you use your lucid dream to manifest the garden you've been cultivating.")    
    drawGarden()
    flower1 = ""
    flower2 = ""
    flower3 = ""
    flower4 = ""
   

def locationSelector() -> None:
    """Selects the location and reads its descriptions."""
    global MemDescSur
    global MemDescAlo
    global MemDescEve
    global MemDescYun
    global location
    global SurDesc
    global AloDesc
    global EveDesc
    global YunDesc
    
    tryAgain: bool = True
    while tryAgain is True:
        tryAgain = False
        print("")
        print(MemDescSur) 
        print(MemDescAlo)
        print(MemDescEve)
        print(MemDescYun)

        location = (int(input("Enter the number of the choice you’d like to select: ")))
        print("")

        if location == 1:
            print("You step forward, and find you’ve set foot on the continent of Sur Tuwan.")
            print("")
            print(SurDesc)
        if location == 2: 
            print("You step forward, and find you’ve set foot on the continent of Alocaysia.")
            print("")
            print(AloDesc)
        if location == 3:
            print("You step forward, and find you’ve set foot on the continent of Everin.")
            print("")
            print(EveDesc)
        if location == 4:
            print("You step forward, and find you’ve set foot on the continent of Yunene.")
            print("")
            print(YunDesc)
        if location > 4:
            print("You do not move, but still find yourself on a vast, empty plane of glass that fades before it reaches the horizon. There is nothing here- no stars, no sand, no rock, no life. Certainly no flowers. You think again about the place you want to see, and hope your dream will manifest it.")
            print("")
            tryAgain = True
        if location <= 0:
            print("You do not move, but still find yourself on a vast, empty plane of glass that fades before it reaches the horizon. There is nothing here- no stars, no sand, no rock, no life. Certainly no flowers. You think again about the place you want to see, and hope your dream will manifest it.")
            print("")
            tryAgain = True

        print("")


def flowerSelector() -> int:
    """Records which flower you look for."""
    floTypes: str = str("🌷🌺🏵 🌼🌻🌸🌹")
    print("What flower will you look for?")
    print(floTypes)
    print("")

    fChoice: int = int(input("Enter the number of the choice you’d like to select: "))
    print("")
    return fChoice


def searchSelector() -> int:
    """Records where the user wants to look and instruts them on places they can look."""
    global Choice1
    global Choice2
    global Choice3
    global SubLocSur1
    global SubLocSur2
    global SubLocSur3
    global SubLocAlo1
    global SubLocAlo2
    global SubLocAlo3
    global SubLocEve1
    global SubLocEve2
    global SubLocEve3
    global SubLocYun1
    global SubLocYun2
    global SubLocYun3

    if location == 1:
        Choice1 = SubLocSur1
        Choice2 = SubLocSur2
        Choice3 = SubLocSur3
    if location == 2:
        Choice1 = SubLocAlo1
        Choice2 = SubLocAlo2
        Choice3 = SubLocAlo3
    if location == 3:
        Choice1 = SubLocEve1
        Choice2 = SubLocEve2
        Choice3 = SubLocEve3
    if location == 4:
        Choice1 = SubLocYun1
        Choice2 = SubLocYun2
        Choice3 = SubLocYun3

    print("Where will you look?")
    print(Choice1)
    print(Choice2)
    print(Choice3)

    SearchLoc: int = int(input("Enter the number of the choice you’d like to select: "))

    print("")

    if SearchLoc > 4:
        SearchLoc = 0
    if SearchLoc < 0:
        SearchLoc = 0

    return SearchLoc 


def exploreResult(SearchLoc: int, fChoice: int) -> None:
    """Gives the result of exploration choices."""
    global minutes
    global location
    global plants
    global SearchResSur1
    global SearchResSur2
    global SearchResSur3
    global SearchResAlo1
    global SearchResAlo2
    global SearchResAlo3
    global SearchResEve1
    global SearchResEve2
    global SearchResEve3
    global patterns
    global flower1
    global flower2
    global flower3
    global flower4
    global FloPlus
    global points

    PatternOrNone: str = str(0)

    if SearchLoc == 0:
        print("You stubbornly sit on the ground and decide to learn nothing, and find nothing. You feel sad, because this took your brain a great deal of effort to make, but gratified, because you were successfully stubborn. Being stubborn does take a while, though.")
        minutes = minutes - 91

    if location == 1:
        minutes = minutes - 90
        plants = plants + "🌴🍃🌿🌱🐚"
        if SearchLoc == 1:
            print(SearchResSur1)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                print("You recorded the pattern.")
                points = points + 5
                patterns = patterns + "፨"
            else:
                print("You decided to move on.")
                points = points + 1
        if SearchLoc == 2:
            print(SearchResSur2)
            print("")
            print("Commit the flower to memory")
            print("Use as inspiration")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                print("You committed the flower to memory.")
                points = points + 5
                if flower1 == "":
                    flower1 = "🌸"
                else:
                    if flower2 == "":
                        flower2 = "🌸"
                    else: 
                        if flower3 == "":
                            flower3 = "🌸"
                        else: 
                            if flower4 == "":
                                flower4 = "🌸"
                            else:
                                print("Wait something’s wrong here")
            if PatternOrNone == "2":
                points = points + 9
                print("You recorded the pattern.")
                patterns = patterns + "❈❁፨"
            if PatternOrNone != "1":
                if PatternOrNone != "2":
                    print("You decided to move on.")
                    points = points + 1
            if fChoice == 6:
                if FloPlus < 3:
                    minutes = minutes + 90
                    FloPlus = FloPlus + 1
        if SearchLoc == 3:
            print(SearchResSur3)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                points = points + 3
                print("You recorded the pattern.")
                patterns = patterns + "፨"
            else:
                print("You decided to move on.")
                points = points + 1

    if location == 2:
        plants = plants + "🌳🍂🍁🍃🌿"
        minutes = minutes - 90
        if SearchLoc == 1:
            print(SearchResAlo1)
            print("")
            print("Commit the flower to memory")
            print("Use as inspiration")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                points = points + 5
                print("You committed the flower to memory.")
                if flower1 == "":
                    flower1 = "🏵 "
                else:
                    if flower2 == "":
                        flower2 = "🏵 "
                    else: 
                        if flower3 == "":
                            flower3 = "🏵 "
                        else: 
                            if flower4 == "":
                                flower4 = "🏵 "
                            else:
                                print("Wait something’s wrong here")
            if PatternOrNone == "2":
                print("You recorded the pattern.")
                points = points + 9
                patterns = patterns + "❃❖❀"
            if PatternOrNone != "1":
                if PatternOrNone != "2":
                    print("You decided to move on.")
                    points = points + 1
            if fChoice == 3:
                if FloPlus < 3:
                    minutes = minutes + 90
                    FloPlus = FloPlus + 1
        if SearchLoc == 2:
            print(SearchResAlo2)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                print("You recorded the pattern.")
                points = points + 3
                patterns = patterns + "❃"
            else: 
                print("You decided to move on.")
                points = points + 1
        if SearchLoc == 3:
            print(SearchResAlo3)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                points = points + 5
                print("You recorded the pattern.")
                patterns = patterns + "❃"
            else: 
                print("You decided to move on.")
                points = points + 1

    if location == 3:
        plants = plants + "🦋🌿🌲🍃"
        minutes = minutes - 90
        if SearchLoc == 1: 
            print(SearchResEve1)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                points = points + 3
                print("You recorded the pattern.")
                patterns = patterns + "❈"
            else: 
                print("You decided to move on.")
                points = points + 1
        if SearchLoc == 2:
            print(SearchResEve2)
            print("")
            print("Commit the flower to memory")
            print("Use as inspiration")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                points = points + 5
                print("You committed the flower to memory.")
                if flower1 == "":
                    flower1 = "🌺"
                else:
                    if flower2 == "":
                        flower2 = "🌺"
                    else: 
                        if flower3 == "":
                            flower3 = "🌺"
                        else: 
                            if flower4 == "":
                                flower4 = "🌺"
                            else:
                                print("You try, but you have no more space in your head to remember another flower.")
            if PatternOrNone == "2":
                print("You recorded the pattern.")
                points = points + 9
                patterns = patterns + "❃❖❀"
            if PatternOrNone != "1":
                if PatternOrNone != "2":
                    print("You decided to move on.")
                    points = points + 1
            if fChoice == 2:
                if FloPlus < 3:
                    minutes = minutes + 90
                    FloPlus = FloPlus + 1
        if SearchLoc == 3:
            print(SearchResEve3)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                points = points + 3
                print("You recorded the pattern.")
                patterns = patterns + "❈"
            else: 
                print("You decided to move on.")
                points = points + 1

    if location == 4:
        plants = plants + "🌾🍀🌱🍃🌿"
        minutes = minutes - 90
        if SearchLoc == 3: 
            print(SearchResYun1)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                print("You recorded the pattern.")
                points = points + 3
                patterns = patterns + "❖"
            else: 
                print("You decided to move on.")
                points = points + 1
        if SearchLoc == 2:
            print(SearchResYun2)
            print("")
            print("Record the pattern")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                print("You recorded the pattern.")
                points = points + 3
                patterns = patterns + "❖"
            else: 
                print("You decided to move on.")
                points = points + 1
        if SearchLoc == 1:
            print(SearchResYun3)
            print("")
            print("Commit the flower to memory")
            print("Use as inspiration")
            print("Move on")
            PatternOrNone = input("Enter the number of the one you’d like to choose: ")
            print("")
            if PatternOrNone == "1":
                print("You committed the flower to memory.")
                points = points + 5
                if flower1 == "":
                    flower1 = "🌷"
                else:
                    if flower2 == "":
                        flower2 = "🌷"
                    else: 
                        if flower3 == "":
                            flower3 = "🌷"
                        else: 
                            if flower4 == "":
                                flower4 = "🌷"
                            else:
                                print("Wait something’s wrong here")
                if PatternOrNone == "2":
                    print("You recorded the pattern.")
                    patterns = patterns + "❃❖❀"
                    points = points + 9
                if PatternOrNone != "1":
                    if PatternOrNone != "2":
                        print("You decided to move on.")
                        points = points + 1
                if fChoice == 1:
                    if FloPlus < 3:
                        minutes = minutes + 90
                        FloPlus = FloPlus + 1


def drawGarden() -> None:
    """Draws the garden."""
    changed1: bool = False
    changed2: bool = False
    changed3: bool = False
    changed4: bool = False
    global flower1
    global flower2
    global flower3
    global flower4
    global patterns
    global plants
    dirt: str = str("〰")

    if patterns != "":
        if flower1 == "":
            flower1 = patterns[randint(0, len(patterns) - 1)] + patterns[randint(0, len(patterns) - 1)]
            changed1 = True
        if flower2 == "":
            flower2 = patterns[randint(0, len(patterns) - 1)] + patterns[randint(0, len(patterns) - 1)]
            changed2 = True
        if flower3 == "":
            flower3 = patterns[randint(0, len(patterns) - 1)] + patterns[randint(0, len(patterns) - 1)]
            changed3 = True
        if flower4 == "":
            flower4 = patterns[randint(0, len(patterns) - 1)] + patterns[randint(0, len(patterns) - 1)]
            changed4 = True
    else: 
        if flower1 == "":
            flower1 = dirt
        if flower2 == "":
            flower2 = dirt
        if flower3 == "":
            flower3 = dirt
        if flower4 == "":
            flower4 = dirt
    
    if plants == "":
        plants = dirt

    print(f"{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{dirt}{dirt}{flower4}{dirt}{dirt}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}")
    print(f"{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{dirt}{dirt}{flower4}{flower3}{flower4}{dirt}{dirt}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}")
    print(f"{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{dirt}{dirt}{flower4}{flower3}{flower2}{flower3}{flower4}{dirt}{dirt}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}")
    print(f"{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{dirt}{dirt}{flower4}{flower3}{flower2}{flower1}{flower2}{flower3}{flower4}{dirt}{dirt}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}")
    print(f"{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{dirt}{dirt}{flower4}{flower3}{flower2}{flower3}{flower4}{dirt}{dirt}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}")
    print(f"{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{dirt}{dirt}{flower4}{flower3}{flower4}{dirt}{dirt}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}")
    print(f"{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{dirt}{dirt}{flower4}{dirt}{dirt}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}{plants[randint(0, len(plants)-1)]}")
    if flower1 == dirt:
        flower1 = ""
    if changed1 is True:
        flower1 = ""
        changed1 = False
    if flower2 == dirt:
        flower2 = ""
    if changed2 is True:
        flower2 = ""
        changed2 = False
    if flower3 == dirt:
        flower3 = ""
    if changed3 is True:
        flower3 = ""
        changed3 = False
    if flower4 == dirt:
        flower4 = ""
    if changed4 is True:
        flower4 = ""
        changed4 = False


if __name__ == "__main__":
    main()