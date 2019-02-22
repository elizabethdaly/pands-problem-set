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
print("The list to check has", len(nums), "elements from.", nums[0], "to", nums[lnum-1])

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
print(ans)
# print(*ans, sep = "\n") # Print each list element on a new line.