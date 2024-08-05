#mammelpop.py
"""
TITLE
DATE
AUTHOR
"""

#imports
from z_myfunc import *
import csv

#variables
FILE = "Elk_island_mammel_population_file.csv"

#inputs
def openFileRead(FILENAME):
    '''
    opens the file and does basic formatting
    :param FILENAME: string
    :return: CONTENT_LIST list
    '''
    FILE = open(FILENAME, newline="")
    CONTENT_LIST = FILE.readlines()
    FILE.close()
    for i in range(len(CONTENT_LIST)): # gets rid of empty lines
        CONTENT_LIST[i] = CONTENT_LIST[i][:-1]
        CONTENT_LIST[i] = CONTENT_LIST[i].split(",")
    return CONTENT_LIST

def file():
    """
    gets the file name the user wants the data from
    :return: str
    """
    print("")
    print("Please Type in File name to access data from: ")
    print("Type (0) for default file")
    FILE = input("> ")
    if FILE == "0":
        FILE = "Elk_island_mammel_population_file.csv"
    return FILE

def menu():
    '''
    Starting Menu Directs user where to go
    :return: OPTION (int)
    '''
    print("Please choose an option:")
    print(" 1. Search Population Growth")
    print(" 2. Add new Year Data")
    print(" 3. Exit ")
    OPTION = input("> ")
    int(OPTION)
    OPTION = checkInt(OPTION)
    if 3 >= OPTION >= 1:
        return OPTION
    else:
        return menu()

def getYearRange():
    """
    gets year range
    :return: int
    """
    print(f"Note: Data stored from 1905 - {ANIMALS[len(ANIMALS)-1][1]} currently")
    print("")
    print("Enter Years Range:")
    YEAR1 = input(" Start Year > ")
    YEAR2 = input(" End Year > ")
    if YEAR1 <= YEAR2 and YEAR1 >= "1905" and YEAR2 <= ANIMALS[len(ANIMALS)-1][1]:
        return YEAR1, YEAR2
    else:
        print("")
        return getYearRange()

def getMammal():
    """
    gets the Mammal
    :return: int
    """
    print("DEER(1), MOOSE(2), ELK(3), BISON(4), ALL(5)")
    MAMMAL = input("> ")
    int(MAMMAL)
    MAMMAL = checkInt(MAMMAL)
    if 5 >= MAMMAL >= 1:
        if MAMMAL == 1:
            return ["Deer"]
        if MAMMAL == 2:
            return ["Moose"]
        if MAMMAL == 3:
            return ["Elk"]
        if MAMMAL == 4:
            return ["Bison"]
        if MAMMAL == 5:
            return ['Deer', 'Moose', 'Elk', 'Bison']
    else:
        return getMammal()

#processing
def searchPopGrowth():
    '''
    Searches (ANIMALS) for Population count of (YEARS)
    :return: float
    '''
    GROWTHRATE = []
    for M in range(len(MAMMAL)):
        for i in range(len(ANIMALS)):
            if ANIMALS[i][1] == YEARARRAY[0] and ANIMALS[i][5] == MAMMAL[M] and ANIMALS[i][0] == "North":
                NSTARTPOP = ANIMALS[i][16]
            if ANIMALS[i][1] == YEARARRAY[1] and ANIMALS[i][5] == MAMMAL[M] and ANIMALS[i][0] == "North":
                NENDPOP = ANIMALS[i][16]

        for i in range(len(ANIMALS)):
            if ANIMALS[i][1] == YEARARRAY[0] and ANIMALS[i][5] == MAMMAL[M] and ANIMALS[i][0] == "South":
                SSTARTPOP = ANIMALS[i][16]
            if ANIMALS[i][1] == YEARARRAY[1] and ANIMALS[i][5] == MAMMAL[M] and ANIMALS[i][0] == "South":
                SENDPOP = ANIMALS[i][16]
            else:
                SSTARTPOP = 0
                SENDPOP = 0
        YEARS = int(YEARARRAY[1]) - int(YEARARRAY[0])
        GROWTH = (int(NENDPOP) + int(SENDPOP) - int(NSTARTPOP) + int(SSTARTPOP)) / int(YEARS)
        GROWTHRATE.append(GROWTH)
    return GROWTHRATE

#outputs

def growthrate():
    if len(MAMMAL) == 1:
        print(f"")
        print(f"Growth Rate of {MAMMAL} Populations: ")
        print(f"    {GROWTH} per Year")
    else:
        print("")
        print(f"Growth Rate of {MAMMAL} Populations: ")
        print(f"    {GROWTH[0]} Deer per Year,\n    {GROWTH[1]} Moose per Year\n    {GROWTH[2]} Elk per Year\n    {GROWTH[3]} Bison per Year")


#main
if __name__ == "__main__":
    while True:
        FILE = file()
        ANIMALS = openFileRead(FILE)
        print("===============================================================")
        print("Welcome to Elk island National park mammal population database!")
        print("")
        OPTION = menu()
        if OPTION == 1:
            YEARARRAY = getYearRange()
            MAMMAL = getMammal()
            GROWTH = searchPopGrowth()
            growthrate()
        if OPTION == 2:
            print("Idk how to do dis")
            print("Cant seem to download the files for new data")
            print("also don't knoew what tis supposed to look like")
        if OPTION == 3:
            exit()



#boop
















