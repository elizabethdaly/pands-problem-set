# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem9.py
#
# Program to read a text file and print every second line.
# The filename is taken from an argument on the command line.
# File is: heaney-poem.txt
# ###########################################################
#
# Describe the program to the user.
print("Program to print every second line from a txt file.")

# sys to get access to command line arguments.
# argv[0] is python script
# argv[1] is file name
import sys

# Use i to keep track of line number, want the odd lines.
i = 1
with open(sys.argv[1], 'r') as f:
    for line in f:
        if i % 2 == 1:
            print("Line", i, ": ", line, end='')
        i = i + 1
        #Data = f.read()
#print(data)

# # fileimport to take filename from command line.
# # Open the file in read mode and print every line.
# import fileinput
# with fileinput.input(mode = 'r') as f:
#     for line in f:
#         print(line, end='')

# # Try opening file from code first and print every line.
# with open('heaney-poem.txt', 'r') as f:
#     for l in f:
#         print(l)
