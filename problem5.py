# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem5.py
#
# Ask the user to input any positve integer.
# Tell the user whether or not the number is a prime.
#
# ###########################################################
#
# Describe the program to the user.
print("Program to check if a given number is a prime.")

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

# Start with some simple checks. =1 or even