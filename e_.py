#e_.py
"""
TITLE
DATE
AUTHOR
"""

import csv

FILENAME = "e_board_games.csv"
FILE = open(FILENAME, newline="")
READER = csv.reader(FILE)

for row in READER:
    print(row)
FILE.close()

NEW_GAME = ["THE CAMPAIGN FOR NORTH AFRICA", " Fight for North Africa in the longest game you could possible imagine", "4.74", "10", "60000"]
FILE = open(FILENAME, "a", newline="")
WRITER = csv.writer(FILE)
WRITER.writerow(NEW_GAME)
FILE.close()


FILE = open(FILENAME, newline="")
READER = csv.reader(FILE)

for row in READER:
    print(", ".join(row))
FILE.close()

FILE.seek(0)

for row in READER:
    print(row)
FILE.close()




















