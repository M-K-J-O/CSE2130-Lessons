#Board.py

'''
Title: Board Game Collection
Author: MARCO OU
Date: I DO NOT KNOW WHAT IM DOING
'''
# --- VARIABLES --- #
FILENAME = "d_board_games.txt"


# --- INPUTS --- #
def menu():
    """Displays a menu of choices for the user to select

    Returns:
        CHOICE (int)
    """
    print("""
What would you like to do?
1. View Collection
2. Add a Game
3. Remove a Game
4. Check Size of the Collection
5. Check games within a range of game length 
6. Check games with # players
7. Search game Titles \" \"
8. Check games within a range of difficulty
9. Save and Exit
    """)
    CHOICE = input("> ")
    return int(CHOICE)


def readFile():
    """Read the data from the file that will be used for the rest of the practice and clean-up.

    Returns:
        DATA_2D (list)
    """
    global FILENAME
    FILE = open(FILENAME)
    DATA = FILE.readlines()
    FILE.close()

    DATA_2D = []
    for i in range(len(DATA)):
        DATA_2D.append(DATA[i].split(","))
        DATA_2D[i][-1] = DATA_2D[i][-1][:-1]  # removes the "\n" character from the end of the last entry of every line

    return DATA_2D


# --- PROCESSING --- #
def fillData(DATA):
    """Ensures each line in the file has the same number of entries

    Args:
        DATA (list): A 2D Array of all of our Data

    Returns:
        DATA (list): Updated version of DATA
    """
    for i in range(len(DATA)):
        for j in range(len(DATA[i])):
            if j > 4:
                DATA.pop(j)
            if j <= 4:
                DATA.append()
            else:
                pass
    writeFile(DATA)
    print("Your collection entries need to be normalized")


def normalizeData(DATA):
    """Converts the data to a standardized format for strings, ints, and floats

    Args:
        DATA (list):

    Returns:
        DATA (list)
    """
    for i in range(len(DATA)):
        str(DATA[i][0])
        str(DATA[i][1])
        int(DATA[i][2])
        int(DATA[i][3])
        int(DATA[i][4])
    print("Your collection values need to be normalized")
    writeFile(DATA)
    return DATA


def addGame(DATA):
    """
    Adds a game to the Collection

    Args:
        DATA (list)
    """

    print("Game Title: ")
    TITLE = input(print(">"))

    print("Description:")
    DESCRIPTION = input(print(">"))

    print("Difficulty:")
    DIFFICULTY = input(print(">"))

    print("Player Count:")
    PLAYERS = input(print(">"))

    print("Average Game Time:")
    TIME = input(print(">"))

    DATA.append(TITLE, DESCRIPTION, DIFFICULTY, PLAYERS, TIME)

    writeFile(DATA)
    print("This function is under construction")


def removeGame(DATA):
    """Removes a game from the collection

    Args:
        DATA (list)
    """

    print("This function is under construction")


def getPlayers(DATA):
    """Tells you how many games of a certain player count are within the collection

    Args:
        DATA (list)
    """

    print("# of Players:")
    PLAYERS = input(print("> "))
    int(PLAYERS)

    for i in range(len(DATA)):
        if DATA[i][4] == PLAYERS:
            print(DATA[i])

    print("This function is under construction")


def getBoardNum(DATA):
    """Tells you how many board games are in the collection

    Args:
        DATA (list)

    Returns:
        LINES (int)
    """

    print(f"Number of Board Games: {len(DATA) + 1}")
    print("This function is under construction")


def getAverageTime(DATA):
    """Tells you the average playtime of games in the collection

    Args:
        DATA (list)
    """
    print("Search Game Length From (Smaller #) to (Bigger #)")
    print("")
    TIMEN = input(print("Smaller > "))
    TIMEP = input(print("Bigger > "))

    for i in range(len(DATA)):
        if DATA[i][2] > TIMEN and DATA[i][2] < TIMEP:
            print(f"{i}. Title:{DATA[i][0]}, Difficulty:{DATA[i][2]}")
    print("This function is under construction")



def getNameRange(DATA):
    """Tells you how many games start with a certain letter

    Args:
        DATA (list)
    """
    print("Enter Game Title")
    TITLE = input(print("> "))

    for i in range(len(DATA)):
        str(DATA[i][0])
        if DATA[i][0] == TITLE:
            print(DATA[i])

    print("This function is under construction")


def getDifficulty(DATA):
    """Tells you how many games there are above or below the selected difficulty level

    Args:
        DATA (list)
    """
    print("Search Difficulty From (Smaller #) to (Bigger #)")
    print("")
    DIFFICULTYN = input(print("Smaller > "))
    DIFFICULTYP = input(print("Bigger > "))

    for i in range(len(DATA)):
        if DATA[i][2] > DIFFICULTYN and DATA[i][2] < DIFFICULTYP:
            print(f"{i}. Title:{DATA[i][0]}, Difficulty:{DATA[i][2]}")

    print("This function is under construction")


# --- OUTPUTS --- #
def intro():
    """Simple message display
    """
    print("Welcome to your Board Game Collection!\n")


def viewData(DATA):
    """Prints out the data in a visually pleasing way

    Args:
        DATA (list): A 2D Array of all of our Data
    """
    for i in range(len(DATA)):
        for j in range(len(DATA[i])):
            if DATA[i][j] != str(DATA[i][j]):
                str(DATA[i][j])
        TEXT = ",".join(DATA[i])
        print(TEXT)


def writeFile(DATA):
    """Writes the changes to the file

    Args:
        DATA (list)
    """
    global FILENAME
    FILE = open(FILENAME, "w")
    DATA_TEXT = ""
    for i in range(len(DATA)):
        DATA_TEXT = DATA_TEXT + ",".join(DATA[i]) + "\n"
    FILE.write(DATA_TEXT)
    FILE.close()
    print("Successfully saved Board Game Collection!")


if __name__ == "__main__":
    DATA = readFile()
    fillData(DATA)
    normalizeData(DATA)
    intro()

    while True:
        CHOICE = menu()
        if CHOICE == 1:  # View Collection
            viewData(DATA)
        elif CHOICE == 2:  # Add a Game
            addGame(DATA)
            normalizeData(DATA)
        elif CHOICE == 3:  # Remove a Game
            removeGame(DATA)
        elif CHOICE == 4:  # Check Size of the Collection
            getBoardNum(DATA)
        elif CHOICE == 5:  # Check Average Playtime of the Collection
            getAverageTime(DATA)
        elif CHOICE == 6:  # Check games with # Players
            getPlayers(DATA)
        elif CHOICE == 7:  # Check games that start with the given character
            getNameRange(DATA)
        elif CHOICE == 8:  # Check games above or below a certain difficulty
            getDifficulty(DATA)
        elif CHOICE == 9:  # Save and Exit
            writeFile(DATA)
            print("Thank you, goodbye!")
            exit()