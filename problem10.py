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

# Import numpy
import numpy as np

# x values are 0 to 4 in steps of 0.5
x = np.arange(0, 4.5, 0.5)

# Customize line/marker styles and use TeX to format labels.
plt.plot(x, x, '-o', label="x")
plt.plot(x, x**2, '--x', label=" $x^2$ ")
plt.plot(x, 2**x, ':D', label=" $2^x$ ")

# Add axis titles.
plt.ylabel('f(x)', fontsize=16)
plt.xlabel('x', fontsize=16)

# Set x axis major ticks to match x values used in calculation. 
plt.xticks(x)

# Set axis limits.
plt.xlim(0,4.5)
plt.ylim(0,18)
# or just make best use of space with tight layout (squashes graph title).
# plt.tight_layout()

# Graph title.
plt.title("Problem 10: Some functions of x", fontsize=18)

# Position legend in good spot wrt these curves.
plt.legend(loc='upper left', fontsize=14)

# Turn on the grid.
plt.grid()

# Save the figure.
plt.savefig('prob10plots.jpeg')

# Show the plot.
plt.show()

###############################################################################
# # Did it with lists first but not versatile.
# #
# # Generate the list of x values.
# xvals = list(range(5))
# print("x values are: ", xvals)

# # Generate list of x squared values.
# xsq = [i**2 for i in xvals]
# print("x squared is", xsq)

# # Generate list of 2^x values.
# pwrx = [2**i for i in xvals]
# print("2 ^ x is", pwrx)

# # Now plot calculated curves.
# # Note that your terminal command line is unresponsive; the show() command 
# # blocks the input of additional commands until you manually kill the plot window.
# plt.plot(xvals, xvals, linestyle='-', marker='.', label='linear')
# plt.plot(xvals, xsq, linestyle='--', marker='x', label='quadratic')
# plt.plot(xvals, pwrx, linestyle=':', marker='D', label='2^x')

# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.title("Some functions of x")
# plt.legend()
# plt.grid()
# plt.show()