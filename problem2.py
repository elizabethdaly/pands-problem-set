# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem2.py
#
# Program to output whether or not today is a day that 
# begins with the letter T
#
# ###########################################################
#
# Describe the program to the user.
print("Program to check if today begins with a T")

# Import Python datetime module
import datetime

# Import Python calendar module for names of weekday.
import calendar

# First of all check what day number it is.
d = datetime.datetime.today().weekday()
print("It's day number", d, ", 0 being Monday")

# Match the integer d to a list containing 7 day names to extract 
# the name of the day. 
# Python does this via day_name[].
dname = calendar.day_name[d]
# print(dname)

# Now check if today begins with T.
# Days beginning with T are 1 (Tuesday) and 3 (Thursday).
if d == 1 or d == 3:
    print("Yes - today begins with a T, it's", dname, ".")
else:
    print ("No - today does not begin with a F, it's", dname, ".")

# An alternative (but more complicated) way to do this would be
# to check if the first letter in the string dname is a "T". 
# type(dname) returns <class 'str'>