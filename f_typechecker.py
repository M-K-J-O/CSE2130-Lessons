#f_typechecker.py
"""
Title POKEmon type checker
Authpr
Date
"""

from z_myfunc import *
# VARIABLES
P_FILE = "pokemon - pokemon.csv"
T_FILE = "types - types.csv"


# INPUTS
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

def getAttackingPokemon():
    """
    Asks for Attacking Pokemon
    :return: string
    """
    print("Your Pokemon:")
    APOKEMON = input(("> "))
    for i in range(len(POKEMON)):
        if APOKEMON != POKEMON[i][1]:
            pass
        if APOKEMON == (POKEMON[i][1]):
            return POKEMON[i]

    print("That is not a Pokemon!")
    return getAttackingPokemon()

def getDefendingPokemon():
    """
    Asks for Defending Pokemon
    :return: string
    """
    print("Opponent's Pokemon:")
    DPOKEMON = input(("> "))
    for i in range(len(POKEMON)):
        if DPOKEMON == POKEMON[i][1]:
            return POKEMON[i]
        if DPOKEMON != POKEMON[i][1]:
            pass
    print("That is not a Pokemon")
    return getDefendingPokemon()

# Proccessing

def typeCheck():
    """
    checks if Attack is super effective/effective/noteffective
    :return: float
    """
    for i in range(len(TYPES)):
        if APOKEMON[2] == TYPES[i][0]:
            ALINE = i
    for i in range(len(TYPES[0])):
        if DPOKEMON[2] == TYPES[0][i]:
            DINDEX = i
    EFFECT = TYPES[ALINE][DINDEX]

    if APOKEMON[3] != "" and DPOKEMON[3] != "":
        for i in range(len(TYPES)):
            if APOKEMON[3] == TYPES[i][0]:
                ALINE = i
        for i in range(len(TYPES[0])):
            if DPOKEMON[3] == TYPES[0][i]:
                DINDEX = i
        EFFECT2 = TYPES[ALINE][DINDEX]
    else:
        EFFECT2 = 1
    if APOKEMON[3] != "":
        for i in range(len(TYPES)):
            if APOKEMON[3] == TYPES[i][0]:
                ALINE = i
        for i in range(len(TYPES[0])):
            if DPOKEMON[2] == TYPES[0][i]:
                DINDEX = i
        EFFECT3 = TYPES[ALINE][DINDEX]
    else:
        EFFECT3 = 1
    if DPOKEMON[3] != "":
        for i in range(len(TYPES)):
            if APOKEMON[2] == TYPES[i][0]:
                ALINE = i
        for i in range(len(TYPES[0])):
            if DPOKEMON[3] == TYPES[0][i]:
                DINDEX = i
        EFFECT4 = TYPES[ALINE][DINDEX]
    else:
        EFFECT4 = 1
    EFFECTF = float(EFFECT) * float(EFFECT2) * float(EFFECT3) * float(EFFECT4)
    return EFFECTF

# Outputs

def effective():
    print(f"EFFECTIVENESS RATING (0% - 1600%)")
    print(f"    0% = No Effect ")
    print(f"    1% - 50% = Not very Effective ")
    print(f"    51% - 100% = Effective ")
    print(f"    101% - 400% = Super Effective ")
    print(f"    401% - 1600% = Super Duper Effective")
    print("")
    print("Your Pokemon Effectiveness rating is:")
    print(f"{EFFECTIVENESS *100}%")

# Main

if __name__ == "__main__":
    while True:
        POKEMON = openFileRead(P_FILE)
        TYPES = openFileRead(T_FILE)
        APOKEMON = getAttackingPokemon()
        DPOKEMON = getDefendingPokemon()
        print("")
        print(f" YOUR POKEMON: {APOKEMON[1]} TYPES: {APOKEMON[2]} {APOKEMON[3]}")
        print(f" OPPONENT'S POKEMON: {DPOKEMON[1]} TYPES: {DPOKEMON[2]} {DPOKEMON[3]}")
        print("")
        EFFECTIVENESS = typeCheck()
        effective()
        print("")
        askContinue()
        print("")

























































