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

# timeit module to measure code exection speed.
from timeit import default_timer as timer

# Request the input.
n = input("Please enter a positive integer: ")

# Check that the input is acually an integer.
# If it's not then quit the program.
# If it is, but is zero or negative, also quit the program.
try:
    int(n)
except ValueError:
    print("Only integers please. Run the program again.")
    quit()
else:
    if int(n) <= 0:
        print("Zero and negative integers not allowed.")
        quit()
    else:
        print("Input is good.")

# Start timer.
ts = timer()

# Create an empty list to store sequence.
collatz = []

# Starting vlaue of while loop & first number in sequence.
n = int(n)
j = n

# Stop when j=1 (saying j>=1 here gives infinite loop).
while j > 1:
    # print(j) # checking
    # If j even do j/2 and store new j
    if j % 2 == 0:          
        j = j/2
        collatz.append(int(j))
    # If j odd do j*3+1 and store new j 
    else:
        j = j*3 + 1
        collatz.append(int(j))
        continue

# Add the original number n to start of list.
collatz.insert(0,n)

# Stop timer.
tf = timer()

# Print the answer
print(collatz)

# and time taken.
print("Time taken:", tf - ts, "s")

# Don't know that there's any obvious pattern, for example:
# n = 10 takes 4.129 e-5 s
# n = 11 takes 5.110 e -5 s
# n = 1000000 takes 29.59 e-5 s
# n = 1000001 takes 20.109 e-5 s