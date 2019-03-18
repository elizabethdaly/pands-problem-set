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
# print(d, "type=", type(d))

# Now try to format it - not quite right using strftime(). 
# strftime options used:
# %A Weekday as full name
# %B Month as full name
# %d Day of month as zero-padded decimal
# %e Day of month NO zero-padding
# %Y Year with century
# %I Hour as zero-padded decimal(12 hour clock)
# %M Minutes
# %p AM/PM
# # Following has no suffix on day, zero pad on hr, PM vs pm.
print(dt.datetime.strftime(d,"%A, %B %e %Y at %I:%M%p"))

# Extract the day of month to generate a suffix.
dom = dt.datetime.now().day
suf = datesuffix(dom)
# print(dom,suf)    # Check.

# Extract hour to generate am/pm lowercase & use 12 hour clock.
# Beware of 12 midday which is 12pm
hr = dt.datetime.now().hour
minute = dt.datetime.now().minute

# am or pm
if hr < 12:
    a = "am"
else:
    a = 'pm'

# 12 hour clock
if hr > 12:
    hr = hr - 12

print(hr, ":", minute, a, sep='') # Check.

# I'll have to separate parts of date for correct formatting.
# Need to keep zero pad on minute, check at hr:0x
print(dt.datetime.strftime(d,"%A, %B %e"), suf, \
dt.datetime.strftime(d," %Y at "), hr, ":", \
dt.datetime.strftime(d,"%M"), a, sep='')