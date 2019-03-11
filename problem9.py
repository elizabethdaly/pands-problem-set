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

# fileimport to take filename from command line.
# Open the file in read mode.
import fileinput
with fileinput.input(mode = 'r') as f:
    for line in f:
        print(line, end='')



# # Use fileinput module to 
# import fileinput
# f = fileinput.input()
# for line in f:
#     print(line)



# # Try opening file from code first and print every line.
# with open('heaney-poem.txt', 'r') as f:
#     for l in f:
#         print(l)
