CSE2130 files and file structure Notes:

Files are used in programs to store data that data is often processed by the program to create information usable by the program or user the main advantage to incorporating files into a program is file persistent which means the data is available beyond the running of the program

files can be used to store default;t settings and start up instructions which can be edited bby an external editor
                   
they can also be used to store information by the program for future use 

another major advantage to impletmenting files is ta\hat thosse fules have structures that insure data integraity data integreity is the degree of reliability of the data 

Crud in text files (acronym) (Create, Read, Use, Delete)

Create tet file 
creating a text file in python will also grant file write privliges 

FILE = open("Filename.ext", "x")

the above function creates a file with the given file name opens it and allows write access. however if there is a file that already exists it will throw a file exists error and stop the python interpreter 

an alrenative is to use the write plus setting 

FILE = open("Filename.ext", "w")

the above methods will overwrite anyinformation with new information 

the program will look for the file relative to its location from the program file most likely this will be the projects root or main folder 

if information needs to be added to the end of the text file used the "a" setting for append. 

close a file
while closing a file is not mandatory the filke will main in computer memory until it is closed therfore to reduce potential memory leaks files should be closed immediatly after they are read or written to 

write to a file

writing to a text file uses the .write string function it can only write strings to the file. 

FILE = open("HELLO-world.txt", "w")
FILE .write("Hellow world")
FILE.close()

reading contents of a text file 

A file that is open in write mode cannot be read and vic versa 

to open a file in read mode use the following: 

FILE = open("filename.ext")
TEXT = FILE.read()
FILE.close
print(TEXT)

When preserving information in each row in a spreadsheet file creating a file line by line insures that the overall structure of the tables is maintainted

FILE = open("filename.ext")
ALIST = FILE.readlines()
\fILE.close
print(A_LISt)

Formatting characters sucg as the \n will be visiable in the strings created frin read liens therefore the data often requires cleanup of unaticipated characters 

updating files

updatating a file requires reading the file to extract the text then making changes to the text and finally overwriting the file with the new text 

FULe + open("fulename.ext")
TEXt = FILE.read()
FILE.close()

process the data in TEXT
FILE = openw(FILEname.ext "w")
FILE.write(text)
FUKE.close()

READ a FILE

FILE = open("filename)
TEXt = FILE.read()
file.close
print(TEXT)

deleting a file

to delete content within a file overwrute the content with a blank string

FILE = open("filename.ext" "w")
FILE.write(")
FILE.close()

to delete a file python requires access to the operatubg systen to exbsyre appropriate fule manage permission

import os
is.remove.filename.ext 

### CSV FILES (Comma Separated Values)

What is a CSV File?
A CSV file is a plane text file that uses commas to delimet its data entries or uses commas to separates its files it is a standadized format making it compatible with many different programs like text editors and spreasheet programs. we can use CSV Files in python by importing the csv libary with import csv 

The first line of a csv file often contains the header or the titles with the associated columns

```
First Name, Last Name, Email
Brain, Hager, brain.hager@epsb.ca
```

using CSV Files

Reading a CSV File

to read the content from a CSV File you need to use CSV.reader this is a iterable object which means we can get through it using a for loop.

```python
FILE = open("Example.csv", newline = "")
READER = csv.reader(FILE) 
for row in READER: 
    print(row)
FILE.close()
```
NOTE: The newline ="" is important in making sure theh formatting of linebreaks in the csv file are correct this parameter can be changed to have different characters stsand in for new lines but for our puposes we can just include the line as is. 

# writing to a sCSV File 
To write to a sxv file we need to use csv.writer(). There are two methods we can use to write to our file, writerow() and writerows(). as the names suggest. writerow() will write to a single line in the file while writerows() can do any # of lines at once.
```python
FILE = open("Example.csv", "w", newline="")
WRITER = csv.writer(FILE)
WRITER.writerow(HEADER) 
WRITER.writerows(DATA)
FILE.close()
```

#### USEFUL FUNCTIONS

FILE.seek()
python and other programming languages treat file objects similiarly it is also easist to imagine them reading through files like we do on the computer with a curser keeping tract of where they currently are normally we read through the entire file at once but it is also possible to read a single line at a time using the newsline() function

If you want to move the curser to a specific location in the file you can use the .seek method seek() takes up 2 parameters seek(offset, from_what)
From_what tels us our reggernece point 
0. the beginning of the file if no offset is specified it is assumed to be 0
1. the current file position
2. the end of the file
3. offset tells the cursor how far from the reference to go.























































