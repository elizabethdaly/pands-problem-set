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

# Generate the list containing the numbers to check.
ns = 1      # start number
ne = 50     # end number

# Rem first element of list is index 0.
nums = list(range(ns,ne + 1))
lnum = len(nums)
print("This list has", len(nums), "elements.")

for x in nums:
    if (x % 6 == 0) and (x % 12 != 0):
        print(x, "divisible by 6 but not by 12")
    else:
        continue


