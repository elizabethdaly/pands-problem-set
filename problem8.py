# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem8.py
#
# Output today's date and time in the format
# "Monday, January 10th 2019 at 1.15pm"
#
# ###########################################################
#
# Describe the program to the user.
print("Program to output today's date in a particular format.")

# Import the Python datetime module.
import datetime as dt

# Just get the date & time first
# d = dt.datetime.today()    # also works
d = dt.datetime.now()
print(d)

# Now try to format it
# Following has no suffix on day, zero pad on hr, PM vs pm. 
print(dt.datetime.strftime(d,"%A, %B%e %Y at %I:%M%p")) 

# strftime options used:
# %A Weekday as full name
# %B Month as full name
# %d Day of month as zero-padded decimal
# %e Day of month NO zero-padding
# %Y Year with century
# %I Hour as zero-padded decimal(12 hour clock)
# %M Minutes
# %p AM/PM