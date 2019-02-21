num = input("Please enter a positive integer: ")
try:
    float(num)
except ValueError:
    print("I said a number!")
else:
    print("Good to go.")
