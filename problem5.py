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

# Import the Python math module.
import math

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
    # else: # Thought there always had to be an else clause, but no.
    #     print("Input is good.")

# Numbet to test.
p = int(n)

# Start with a simple check: is p=1 or even? Also dismiss p=2.
if p == 1 or p % 2 == 0 or p == 2:
    print("1 and even numbers (except 2) are not prime.")
    quit()

# So now we know the number is !=2, odd, and > 1.

# Use a version of trial division: divide p by all odd numbers =< floor(sqrt(n)).
# Really should try dividing by all primes less than this limit, but I assume 
# we don't know them.
# Could same some time by not trying multiples of 3, 5, 7, 11 etc.
# Might be worth trying if testing huge numbers.

z = math.floor(math.sqrt(p))
print("Test limit = ", z)

# Try division only by the odd numbers <= z.
print("Checking for division by", len(range(3,z + 1, 2)), "number(s).")
for x in range(3, z + 1, 2):
    # print("x = ", x)
    if p % x == 0:
        print(p, "is not a prime as", p, "/", x, "=", int(p/x))
        # Stop testing once a factor is found.
        break
# Or terminate loop as list exhausted. 
else:
    print(p, "is prime.")

# print("Finished testing")

# Test program with some big primes: 7919, 105943, 179,426,549
# It works fine and seems instantaneous.
# Eg. 179,426,549 tests for division by 6697 odd numbers up to 13,395 