# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem1.py
# Ask the user to input any positve integer
# Output the sum of all numbers between one and that number
#
# ###########################################################
#
# Request the input
n = int(input("Please enter a positive integer: "))
print(n)

# Check if n is a positive integer
# break to exit loop, quit() to exit program
if n == 0 or n < 0:
    print("Input must be positive integer")
    quit()
else:
    print("Input is good")

# Generate a list containing the numbers from 1 to n
numlist = list(range(1,n+1))
print(numlist)

# Sum the elements in the list
ans = sum(numlist)
print("The sum of all numbers from 1 to", n, "is: ", ans)

# Still get error if enter 1.5, need to fix: type()