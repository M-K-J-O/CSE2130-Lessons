"""
Author
Title
Date
"""
#creatning a file
FILENAME = "crud.txt"
FILE = open(FILENAME, "w")



FILE.write("Hello World \n")


FILE = open(FILENAME, "a")
FILE.write("GOOD AFTERNOOON")
FILE.close()

#READ a FILE

FILE = open(FILENAME)
TEXT = FILE.read()
FILE.close()
print(TEXT)

#READ A FULE LINE BY LINE

FILE = open(FILENAME)
A_LIST = FILE.readlines()
FILE.close()
print(A_LIST)

for i in range(len(A_LIST)):
    if i != len(A_LIST) - 1:
        A_LIST[i] = A_LIST[i][:-1]
print(A_LIST[i])

import os
os.remove(FILENAME)





