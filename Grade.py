"""
Title
Date
Author
"""

from z_myfunc import *
import os

# Variables

FILENAME = "g_text.txt"


# iNPUTS
def menu():
    '''
    user chooses operation
    :return: CHOICE: (int)
    '''
    print("""
    
1. View Grades
2. Add New Subject
3. Update Subject Grade 
4. Delete Subject 
5. Calculate Average 
6. Exit

    """)

    CHOICE = checkInt(input("> "))
    if 0 < CHOICE < 7:
        return CHOICE
    else:
        print("Please enter a number in the menu")
        return menu()


def getFileRead():
    """
    Open grade file and create one if doesnt exist
    :return: FILE (Object)
    """
    global FILENAME
    try:
        FILE = open(FILENAME, "x")
        START_GRADE = []
        for i in range(10):
            START_GRADE.append("--- 00")
        START_GRADE_TEXT = ",".join(START_GRADE)
        FILE.write(START_GRADE_TEXT)
        FILE.close()
    except FileExistsError:
        pass
    else:
        os.remove("g_text.txt")
        FILE = open(FILENAME, "x")
        START_GRADE = []
        for i in range(10):
            START_GRADE.append("--- 00")
        START_GRADE_TEXT = ",".join(START_GRADE)
        FILE.write(START_GRADE_TEXT)
        FILE.close()
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


def getGrade():
    """
    Get the Students Grade
    :return: GRADE: (int)
    """
    GRADE = checkInt(input("GRADE: "))
    return GRADE

def getSubject():
    '''
    asks user for Subject Name
    :return: (string)
    '''
    print("NOTE: Subject must have no spaces letters!")
    SUBJECT = input("SUBJECT: ")
    SUBJECT = SUBJECT.replace(" ", "_")
    return SUBJECT

# PROCESSING

def readFile(FILE_OBJ):
    '''
    reading contents of file
    :param FILE_OBJ: (object)
    :return: GRADE_ARRAY: (list)
    '''

    TEXT = FILE_OBJ.read()
    FILE_OBJ.close()
    GRADE_ARRAY = TEXT.split(",")
    return GRADE_ARRAY

def updateNewGrade(GRADE, SUBJECT, GRADE_ARRAY):
    """
    updates grade list with the new grade
    :param GRADE: (int)
    :param SUBJECT: (string)
    :param GRADE_ARRAY: (list)
    :return: (list)
    """
    GRADE_ARRAY_2D = []
    for i in range(len(GRADE_ARRAY)):
        GRADE_ARRAY_2D.append(GRADE_ARRAY[i].split())
        GRADE_ARRAY_2D[-1][1] = int(GRADE_ARRAY_2D[-1][1])

    for i in range(len(GRADE_ARRAY)):
        if GRADE > GRADE_ARRAY_2D[i][1]:
            GRADE_ARRAY.insert(i, f"{SUBJECT} {GRADE}")
            GRADE_ARRAY.pop()
            return GRADE_ARRAY

def checkNewGrade(GRADE, GRADE_ARRAY):
    '''
    tests if score is High
    :param GRADE: (int)
    :param GRADE_ARRAY: (list)
    :return: (bool)
    '''

    GRADE_ARRAY_2D = []
    # creates a 2d array with the scores set as integers
    for i in range(len(GRADE_ARRAY)):
        GRADE_ARRAY_2D.append(GRADE_ARRAY[i].split())
        GRADE_ARRAY_2D[-1][1] = int(GRADE_ARRAY_2D[-1][1])

    for i in range(len(GRADE_ARRAY_2D)):
        if GRADE > GRADE_ARRAY_2D[i][1]:
            return True
    return False

def updateGrade(GRADE, SUBJECT, GRADE_ARRAY):
    """
    updates grade list with the new grade
    :param GRADE: (int)
    :param SUBJECT: (string)
    :param GRADE_ARRAY: (list)
    :return: (list)
    """
    GRADE_ARRAY_2D = []
    for i in range(len(GRADE_ARRAY)):
        GRADE_ARRAY_2D.append(GRADE_ARRAY[i].split())
        GRADE_ARRAY_2D[-1][1] = int(GRADE_ARRAY_2D[-1][1])

    for i in range(len(GRADE_ARRAY)):
        if SUBJECT == GRADE_ARRAY_2D[i][1]:
            GRADE_ARRAY.replace(i, f" {GRADE}")
            GRADE_ARRAY.pop()
            return GRADE_ARRAY

# OUTPUTS

def viewGrades(GRADES):
    """
    display the GRADES
    :param GRADES: (list)
    """
    print("SUBJECTS | GRADES (%)")
    for i in range(len(GRADES)):
        print(f"{i + 1}. {GRADES[i]}")


def writeFile(FILE_OBJ, GRADE_ARRAY):
    """
    writes the changes to the file
    :param FILE_OBJ: (obj)
    :param GRADE_ARRAY: (list)
    """
    GRADE_TEXT = ",".join(GRADE_ARRAY)
    FILE_OBJ.write(GRADE_TEXT)
    FILE_OBJ.close()
    print("Successfully saved Grade!")


# maincode


if __name__ == "__main__":
    FILE = getFileRead()
    GRADES = readFile(FILE)
    ITEM = 0
    while True:
        CHOICE = menu()
        if CHOICE == 1:
            viewGrades(GRADES)
        elif CHOICE == 2:
            GRADE = getGrade()
            SUBJECT = getSubject()
            GRADES = updateNewGrade(GRADE, SUBJECT, GRADES)
            FILE = getFileWrite()
            writeFile(FILE, GRADES)
            pass
        elif CHOICE == 3:
            GRADE = getGrade()
            SUBJECT = getSubject()
            GRADES = updateGrade(GRADE, SUBJECT, GRADES)
            FILE = getFileWrite()
            writeFile(FILE, GRADES)
            pass
        elif CHOICE == 4:
            pass
        elif CHOICE == 5:
            pass
        elif CHOICE == 6:
            exit()
