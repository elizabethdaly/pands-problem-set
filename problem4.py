# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem4.py
#
# Program that asks the user to input any positive integer and outputs the successive values of the following 
# calculation. At each step calculate the next value by taking  the current calue and, if it is even, divide 
# by two, but if it is odd, multiply by three and add one. Have the progam end if the current value is one.
# ###########################################################
#
# Describe the program to the user.
print("Program to print the Collatz sequence of a number n.")

# Request the input.
num = input("Please enter a positive integer: ")

# Check that the input is acually an integer.
# If it's not then quit the program.
# If it is, but is zero or negative, also quit the program.
try:
    int(num)
except ValueError:
    print("Only integers please. Run the program again.")
    quit()
else:
    if int(num) <= 0:
        print("Zero and negative integers not allowed.")
        quit()
    else:
        print("Input is good.")

