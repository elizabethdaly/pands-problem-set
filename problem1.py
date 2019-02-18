# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem1.py
# Ask the user to input any positve integer
# Output the sum of all numbers between one and that number
#
# ###########################################################
#
# Describe the program
print("Program to find the sum of all numbers from 1 to a number",
"-digits to right of decimal point are discarded", sep="\n")

# Request the input, for now assume a number
num = input("Please enter a positive integer: ")
numflt = float(num)
# print (numflt, type(numflt))

n = int(numflt) # Keep only integer part of number
# print(n, type(n))

# Check if n is a positive integer
# break to exit loop, quit() to exit program
if n == 0 or n < 0:
    print("Input must be a positive integer")
    quit()
else:
    print("Input is good")

# Generate a list containing the numbers from 1 to n
numlist = list(range(1,n+1))
# print(numlist)

# Sum the elements in the list
ans = sum(numlist)
print("The sum of all numbers from 1 to", n, "is: ", ans)

# Program now handles floats, 0, -ve