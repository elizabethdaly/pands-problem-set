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

# Import Python calendar module
import calendar

# First of all check what day number it is.
d = datetime.datetime.today().weekday()
print("It's day number", d, ", 0 being Monday")

# Could just match the integer d to a list containing 7 day names
# to extract the name of the day. Python does this via day_name[].
dname = calendar.day_name[d]
print("It's ",dname)

# Now check if today begins with T.