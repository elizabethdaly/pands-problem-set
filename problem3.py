# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem3.py
#
# Program to print all numbers between 1,000 and 10,000
# that are divisible by 6 but not by 12.
# ###########################################################
#
# Describe the program to the user.
print("Program to print all numbers between 1,000 and 10,000",  
"that are divisible by 6 but not by 12.", sep="\n")

# What are the numbers?
ns = 1000   # start number
ne = 10000  # end number

# Generate the list containing the numbers to check.
# Rem first element of list is index 0, last is length-1.
# Check that first and last numbers are correct
nums = list(range(ns,ne + 1))
lnum = len(nums)
print("The list to check has", len(nums), "elements from", nums[0], "to", nums[lnum-1])

# timeit module to measure code exection speed.
from timeit import default_timer as timer

######################################
#
# Original solution that works fine.
#
######################################

# Start timer.
ts = timer()

# Create an empty list to hold the answer.
ans = []

# If both conditions are true (/6 AND not /12) put number in new list)
for x in nums:
    if (x % 6 == 0) and (x % 12 != 0):
        # print(x, "divisible by 6 but not by 12")
        ans.append(x)
    else:
        continue

lans = len(ans)
print(lans, "numbers are divisible by 6 but not by 12. They are:")

# Stop timer.
tf = timer()

print("Time taken:", tf - ts, "s")
print(ans)
# print(*ans, sep = "\n") # Print each list element on a new line.

############################################################################################
# Another way to do this would be to cycle through all the numbers from 1000 to 10000
# and generate a new list containing only those divisible by 6.
# The second condition (is number divisible by 12) could then be checked on this shorter list.
# 
# I tried running both methods (- print statements) and using timer(). There was very little 
# difference in time taken between the two methods, with no consistent trend. 
# A non-trivial calculation might show a difference.
############################################################################################

# # Start timer.
# t1 = timer()

# # Create an empty list to store the numbers divisible by 6.
# ans6 = []

# # Generate that list.
# for x in nums:
#     if x % 6 == 0:
#         ans6.append(x)
#     else:
#         continue

# print(len(ans6), "numbers are divisible by 6.")

# # Create another empty list to store the numbers divisible by 6 but not by 12.
# ans6not12 = []

# # Generate that list.
# for y in ans6:
#     if y % 12 != 0:
#         ans6not12.append(y)
#     else:
#         continue
# print(len(ans6not12), "of these are also not divisible by 12.")

# # Stop timer.
# t2 = timer()
# print("Time:", t2 - t1, "s")

# print("These are:", ans6not12)