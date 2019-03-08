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

# Number to test.
s = float(n)

# Babylonian Method: if x is an overestimate of sqrt(s), then s/x will be
# an under estimate, and the average of both quantities will be an even better
# estimate. repeat until desired accuracy achieved.
# Quadratically convergent: number of correct digits in approximation doubles
# with each iteration.
# Initial guess required: best if close to s.

# Maximum number of iterations allowed.
iter = 20

# Required accuracy.
# Difference actually goes to 0.0 so make tol very small.
tol = 0.0000001

# Initial guess for the square root, the closer to s the better.
x = 2*s

# Start loop counter
i = iter
while i > 0:
    # Calculate estimate.
    xi = 0.5*(x + s/x)

    # How close is new estimate to last one? If less than tol then stop.
    # print("i=", i, "x=", x, "xi=",xi, "Diff=", abs(xi-x))
    if abs(xi-x) <= tol:
        break
    
    # Refine your guess for next iteration.
    x = xi
    
    # Decrement loop counter.
    i = i - 1

print("The square root of", s, "is approximately", round(xi,2))
print("Number of iterations:", (iter - i + 1))