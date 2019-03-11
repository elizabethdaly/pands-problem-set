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

#############################################################
# Define a function to generate the suffix for day of month.
def datesuffix(n):
    """Given day of month return English Ordinal Suffix"""
    if (n == 1 or n == 21 or n == 31):
        suffix = "st"
    elif (n == 2 or n == 22):
        suffix = "nd"
    elif (n == 3 or n == 23):
        suffix = "rd"
    else:
        suffix = "th"
    return suffix

# # Test that function works correctly.
# i = 1
# while i < 32:
#     print(i, datesuffix(i))
#     i = i + 1
#############################################################

# Just get the date & time first
d = dt.datetime.now()
print(d, "type=", type(d))

# Now try to format it - not quite right.
# Following has no suffix on day, zero pad on hr, PM vs pm. 
# strftime options used:
# %A Weekday as full name
# %B Month as full name
# %d Day of month as zero-padded decimal
# %e Day of month NO zero-padding
# %Y Year with century
# %I Hour as zero-padded decimal(12 hour clock)
# %M Minutes
# %p AM/PM
print(dt.datetime.strftime(d,"%A, %B %e %Y at %I:%M%p"))

# Extract the day of month to generate a suffix
dom = dt.datetime.now().day
suf = datesuffix(dom)
print(dom,suf)

# Extract hour to generate am/pm lowercase & 12 hour clock.
hr = dt.datetime.now().hour

if hr < 12:
    a = "am"
else:
    a = "pm"
    hr = hr - 12
print(hr,a)

# Think I'll have to separate date into parts for correct formatting.
print(dt.datetime.strftime(d,"%A, %B %e"), suf, dt.datetime.strftime(d,"%Y at"))
print(dt.datetime.strftime(d,"%I:%M"), a)

