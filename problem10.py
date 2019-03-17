# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem10.py
#
# Plot the functions x, x^2, and 2^x in the range [0, 4].
#
# ###########################################################
#
# Describe the program to the user.
print("Program to plot some functions.")

# Import matplotlib.
import matplotlib.pyplot as plt

# Import numpy for computation.
import numpy as np

# Generate the list of x values.
xvals = list(range(5))
print("x values are: ", xvals)

# Generate list of x squared values.
xsq = [i**2 for i in xvals]
print("x squared is", xsq)

# Get started. Prompt doesn't come back until figure window closed.
plt.plot(xvals)
plt.ylabel('y')
plt.xlabel('x')
plt.show()

# will need exp2 for 2**p with p input array
# might need to save plots/ plot if all on one figure
# annotate [plots x, x^2, 2^x]