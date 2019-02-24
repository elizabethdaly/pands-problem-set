# pands-problem-set
## Elizabeth Daly
### January-April 2019
### HDip Data Analytics 2019 Programming and Scripting Problem Set

Git-hub depository at:
https://github.com/elizabethdaly/pands-problem-set.git


## Problem 1
**File:** problem1.py

Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

Python tutorial 3.1.1 for the different types of numbers
https://docs.python.org/3/tutorial/introduction.html#numbers

I used stackoverflow to investigate how to reject incorrect keyboard input:
https://stackoverflow.com/a/5424739

I decided to accept all numbers initially. Then negative numbers and 0 are rejected, and the decimal part of floats is discarded.

## Problem 2
**File:** problem2.py

Write a program that outputs whether or not today is a day that begins with the letter T.

Python tutorial for:
* datetime module: https://docs.python.org/3/library/datetime.html#module-datetime
* calendar module: https://docs.python.org/3/library/calendar.html#module-calendar

I used stackoverflow to check how to extract the day name from the 
day of week integer that datetime returns:
https://stackoverflow.com/a/36341648

## Problem 3
**File:** problem3.py

Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not by 12.

I first approached it by generating a list containing all the numbers to check. Both conditions were checked at the same time, is number divisible by 6 AND not by 12? I stored the answer in a new list.
I also wrote the program to check the first condition on the original list, is number divisible by 6? I then checked the second condition on the shorter list, is number NOT divisible by 12? Not sure which is better/faster, but both work. I checked time taken for each method but couldn't find consistent difference. Code for original solution is neater.

Python tutorial for timeit module to measure code execution speed: https://docs.python.org/3/library/timeit.html?highlight=timeit#module-timeit

## Problem 4
**File:** problem4.py

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking  the current calue and, if it is even, divide by two, but if it is odd, multiply by three and add one. Have the progam end if the current value is one.

As in problem 1, I used try-except-else to reject input that is not of type int. If the input is an integer
I then check to make sure it's not zero or negative.

Looked up how to add an element to the beginning of a list on stackoverflow: https://stackoverflow.com/a/17911209



