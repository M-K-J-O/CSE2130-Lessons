"""
Title
Date
Author
"""

from z_myfunc import *

# Variables

FILENAME = "b_text.txt"


# iNPUTS
def menu():
    '''
    user chooses operation
    :return: CHOICE: (int)
    '''
    print("""
1. View Score
2. Add New Score
3. Exit
    
    """)

    CHOICE = checkInt(input("> "))
    if 0 < CHOICE < 4:
        return CHOICE
    else:
        print("Please enter a number in the menu")
        return menu()

def getFileRead():
    """
    Open score file and create one if doesnt exist
    :return: FILE (Obeject)
    """
    global FILENAME
    try:
        FILE = open(FILENAME, "x")
        START_SCORE = []
        for i in range(10):
            START_SCORE.append("AAA 0")
        START_SCORE_TEXT = "," .join(START_SCORE)
        FILE.write(START_SCORE_TEXT)
        FILE.close()
    except FileExistsError:
        pass

    FILE = open(FILENAME)
    return FILE

def getFileWrite():
    """
    Opens the file in write state
    :return: FILE: (Obj)
    """
    global FILENAME
    FILE = open(FILENAME, "w")
    return FILE

def getScore():
    """
    Get the players score
    :return: SCORE: (int)
    """
    SCORE = checkInt(input("SCORE: "))
    return SCORE

def getName():
    '''
    asks user for name
    :return: (string)
    '''
    print("NOTE: name must be 3 letters!")
    NAME = input("NAME: ")
    NAME = NAME.upper()
    if len(NAME) > 3:
        NAME = NAME[:3]
    return NAME



# PROCESSING

def readFile(FILE_OBJ):
    '''
    reading contents of file
    :param FILE_OBJ: (object)
    :return: SCORE_ARRAY: (list)
    '''

    TEXT = FILE_OBJ.read()
    FILE_OBJ.close()
    SCORE_ARRAY = TEXT.split(",")
    return SCORE_ARRAY

def checkNewScore(SCORE, SCORE_ARRAY):
    '''
    tests if score is High
    :param SCORE: (int)
    :param SCORE_ARRAY: (list)
    :return: (bool)
    '''

    SCORE_ARRAY_2D = []
    # creates a 2d array with the scores set as integers
    for i in range(len(SCORE_ARRAY)):
        SCORE_ARRAY_2D.append(SCORE_ARRAY[i].split())
        SCORE_ARRAY_2D[-1][1] = int(SCORE_ARRAY_2D[-1][1])

    for i in range(len(SCORE_ARRAY_2D)):
        if SCORE > SCORE_ARRAY_2D[i][1]:
            return True
    return False

def updateHighScore(SCORE, NAME, SCORE_ARRAY):
    """
    updates score list with the new score
    :param SCORE: (int)
    :param NAME: (string)
    :param SCORE_ARRAY: (list)
    :return: (list)
    """
    SCORE_ARRAY_2D = []
    for i in range(len(SCORE_ARRAY)):
        SCORE_ARRAY_2D.append(SCORE_ARRAY[i].split())
        SCORE_ARRAY_2D[-1][1] = int(SCORE_ARRAY_2D[-1][1])

    for i in range(len(SCORE_ARRAY)):
        if SCORE > SCORE_ARRAY_2D[i][1]:
            SCORE_ARRAY.insert(i, f"{NAME} {SCORE}")
            SCORE_ARRAY.pop()
            return SCORE_ARRAY



# OUTPUTS

def viewScores(SCORES):
    """
    display the scores
    :param SCORES: (list)
    """
    print("High Scores!")
    for i in range(len(SCORES)):
        print(f"{i+1}. {SCORES[i]}")

def writeFile(FILE_OBJ, SCORE_ARRAY):
    """
    writes the changes to the file
    :param FILE_OBJ: (obj)
    :param SCORE_ARRAY: (list)
    """
    SCORE_TEXT = ",".join(SCORE_ARRAY)
    FILE_OBJ.write(SCORE_TEXT)
    FILE_OBJ.close()
    print("Successfully saved High Score!")
# maincode


if __name__ == "__main__":
    FILE = getFileRead()
    SCORES = readFile(FILE)
    while True:
        CHOICE = menu()
        if CHOICE == 1:
            viewScores(SCORES)
        elif CHOICE == 2:
            SCORE = getScore()
            if checkNewScore(SCORE, SCORES):
                print("HIGH SCORE!")
                NAME = getName()
                SCORES = updateHighScore(SCORE, NAME, SCORES)
                FILE = getFileWrite()
                writeFile(FILE, SCORES)
            pass
        elif CHOICE == 3:
            exit()



















