# Elizabeth Daly
# HDip Data Analytics 2019 pands-problem-set
# 
# problem6.py
#
# Ask the user to input any string.
# Output every second word.
#
# ###########################################################
#
# Describe the program to the user.
print("Program to print every second word of a sentence.")

# Request the input.
s = input("Please enter a short sentence: ")
# print("Input", s, type(s))

# Replace any , in sentence with nothing, ie remove them.
# Could do same for other common punctuation marks; :
a = s.replace(',', '')
# print(a)

# Remove the full stop (or ?!) if there is one.
b = a.rstrip('.?!')
# print(b)

# Now split the sentence into a list of its words.
c = b.split()
# print(c)
# print(len(c))

# Make a new list of desired words (every second). 
d = c[0::2]
# print(d)

# Convert list to a string and print.
e = ' '.join(d)
print(e)

# ##################################################################################
# # Solution I originally had was to print out words in a loop; one above is neater.
# #
# # Print every second word in the sentence starting with the first one.
# # Don't go to a new line, just insert a space between the words.
# for i in range(0, len(c), 2):
#     print(c[i], end=' ')