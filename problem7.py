# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem7.py
#
# Ask the user to input any positve floating point number.
# Output an estimate of its square root.
#
# ###########################################################
#
# Describe the program to the user.
print("Program to estimate the square root of a number.")

# Request the input.
n = input("Please enter a positive number: ")

# Check that the input is a floating point number.
# If it's not then quit the program.
# If it is, but is zero or negative, also quit the program.
try:
    float(n)
except ValueError:
    print("Only numbers please. Run the program again.")
    quit()
else:
    if float(n) <= 0:
        print("Zero and negative numbers not allowed.")
        quit()

# Numbet to test.
s = float(n)

# Babylonian Method. Quadratically convergent. Initial guess required.