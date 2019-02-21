# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem1.py
#
# Ask the user to input any positve integer
# Output the sum of all numbers between one and that integer
#
# ###########################################################
#
# Describe the program to the user.
print("Program to find the sum of all numbers from 1 to a given number",
"- digits to right of decimal point are discarded", sep="\n")

# Request the input.
num = input("Please enter a positive integer: ")

# Check that the input is acually a number.
# If it's not then quit the program.
# I want to allow any number at this stage, not just integers.
try:
    float(num)
except ValueError:
    print("Only numbers please. Run the program again.")
    quit()
else:
    # Convert raw input to a float
    numflt = float(num)

# Check type of numflt.
# print (numflt, type(numflt))

# Keep only the integer part of the number, ie round down.
n = int(numflt) 
# print(n, type(n))

# Check if n is a positive integer
# If it's not, quit() to exit program (break would exit loop only)
if n == 0 or n < 0:
    print("Input must be a positive integer")
    quit()
else:
    print("Input is good")

# Now calculate the sum.

# Generate a list containing the numbers from 1 to n.
numlist = list(range(1,n+1))
# print(numlist)

# Sum the elements in the list
ans = sum(numlist)
print("The sum of all numbers from 1 to", n, "is: ", ans)

# Program handles floats, 0, and -ve numbers. It rejects letters.