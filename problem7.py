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
# estimate. Repeat until desired accuracy achieved.
# Quadratically convergent: number of correct digits in approximation doubles
# with each iteration.
# Initial guess required: best if close to sqrt(s).

# Maximum number of iterations allowed.
iter = 100

# Required accuracy.
# Difference actually goes to 0.0 so make tol very small.
tol = 0.0000001

# Initial guess for the square root, the closer to sqrt(s) the better.
# As the best guess depends on the number, s, one could ask the user to
# provide it. To keep things simple, I'm going to pick a default value.
x = 0.1*s

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

# Test program with s = 123456789.12
# Answer = 11111.11
# Guess = 0.1*s, iterations taken = 15 (If s=100, sqrt(s)=0.1*s)
# Guess = s/2, iterations taken = 18 (If s=4, sqrt(4)=s/2)
# Guess = s, iterations taken = 19 (If s=1, sqrt(1)=1)
# Guess = 2*s, iterations taken = 20 (A ridiculous guess!)

# Test program with s = 0.123456789
# Answer = 0.35
# Guess = 0.1*s, iterations taken = 9
# Guess = s/2, iterations taken = 7
# Guess = s, iterations taken = 6
# Guess = 2*s, iterations taken = 5
# So best guess depends on value of s. I'll leave 0.1s by default.