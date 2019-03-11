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

# sys module to get access to command line arguments.
# argv[0] is the Python script [problem9.py]
# argv[1] is the file name [heaney-poem.txt]
# To run type: python problem9.py heaney-poem.txt
import sys

# Use i to keep track of line number, want the odd lines only.
i = 1
# Use with to ensure file is closed when you are finished with it.
with open(sys.argv[1], 'r') as f:
    for line in f:
        if i % 2 == 1:
            print("Line", i, ": ", line, end='')
        i = i + 1

# First attempts below
#
# # fileimport module to take filename(s) from command line.
# # Open the file in read mode and print every line.
# import fileinput
# with fileinput.input(mode = 'r') as f:
#     for line in f:
#         print(line, end='')

# # Try opening file from within the script first and print every line.
# with open('heaney-poem.txt', 'r') as f:
#     for l in f:
#         print(l)