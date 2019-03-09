# pands-problem-set
## Elizabeth Daly
### January-April 2019
### HDip Data Analytics 2019 Programming and Scripting Problem Set

Git-hub depository at:
https://github.com/elizabethdaly/pands-problem-set.git


## Problem 1
**File:** problem1.py

**Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.**

Python tutorial 3.1.1 for the different types of numbers:
https://docs.python.org/3/tutorial/introduction.html#numbers

I used stackoverflow to investigate how to reject incorrect keyboard input:
https://stackoverflow.com/a/5424739

I decided to accept all numbers initially. Then negative numbers and 0 are rejected, and the decimal part of floats is discarded.

## Problem 2
**File:** problem2.py

**Write a program that outputs whether or not today is a day that begins with the letter T.**

Python tutorial for:
* datetime module: https://docs.python.org/3/library/datetime.html#module-datetime
* calendar module: https://docs.python.org/3/library/calendar.html#module-calendar

I used stackoverflow to check how to extract the day name from the 
day of week integer that datetime returns:
https://stackoverflow.com/a/36341648

## Problem 3
**File:** problem3.py

**Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not by 12.**

I first approached it by generating a list containing all the numbers to check. Both conditions were checked at the same time, is number divisible by 6 AND not by 12? I stored the answer in a new list.
I also wrote the program to check the first condition on the original list, is number divisible by 6? I then checked the second condition on the shorter list, is number NOT divisible by 12? Not sure which is better/faster, but both work. I checked time taken for each method but couldn't find consistent difference. Code for original solution is neater.

Python tutorial for timeit module to measure code execution speed: https://docs.python.org/3/library/timeit.html?highlight=timeit#module-timeit

## Problem 4
**File:** problem4.py

**Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking  the current value and, if it is even, divide by two, but if it is odd, multiply by three and add one. Have the progam end if the current value is one.**

As in problem 1, I used try-except-else to reject input that is not of type int. If the input is an integer I then check to make sure it's not zero or negative.

Looked up how to add an element to the beginning of a list on stackoverflow: https://stackoverflow.com/a/17911209

## Problem 5
**File:** problem5.py

**Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.**

I used try-except-else to reject input that is not a positive integer. I then dismiss 1 and all even numbers apart from 2.

I researched primes & primality tests in a few places:
* Wikipedia: https://en.wikipedia.org/wiki/Prime_number
* The Sieve of Eratosthenes: http://mathforum.org/dr.math/faq/faq.prime.num.html
* The trial division test: https://www.wikihow.com/Check-if-a-Number-Is-Prime
which involves dividing the number (n) by each prime to floor(sqrt(n)). The drawback of this method is that it requires one to know the primes up to floor(sqrt(n)); I assume we don't know those. As a compromise, I will attempt to divide n by all odd numbers from 3 up to that limit instead. Could save some time by avoiding multiples of some of those odd numbers that we know are prime: 3, 5, 7, 11, 13, 17, etc.

## Problem 6
**File:** problem6.py

**Write a program that takes a user input string and outputs every second word.**
λ python problem6.py
Program to print every second word of a sentence.
Please enter a short sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog

## Problem 7
**File:** problem7.py

**Write a program that takes a positive floating point number as input and outputs an approximation of its square root.**

I researched methods of estimating square roots and found some interesting links:
* Khan Academy: https://www.khanacademy.org/math/pre-algebra/pre-algebra-exponents-radicals/pre-algebra-square-roots/v/approximating-square-roots
This method is based on finding the closest perfect squares (less than and greater than) the number. I am assuming that we don't necessarily know those, and certainly not for big numbers. Conclude that this method is more suited to a manual calculation and small numbers.
* The digit by digit method: https://en.wikipedia.org/wiki/
Methods_of_computing_square_roots#Digit-by-digit_calculation
This method finds each digit of the square root in a sequence. It's slower than the Babylonian method below and perhaps better for manual calculations.
* The Babylonian method: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
Briefly, if x is an overestimate of the square root of n, then n/x is an underestimate. The average of these two estimates will be a better approximation. 
* The Bakhshali method: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
Similar to the Babylonian method except that each iteration here is equivalent to two iterations of the previous algorithim. Therefore, this method converges faster (quartically rather than quadratically) to a solution. More calculations are required per loop iteration, so I decided against it unless I ran into convergence problems. 

I used the **Babylonian** method as only one calculation per loop iteration is required. An initial guess for the square root must be provided. This could be provided by the user but I picked a default value to keep things simple. Ideally that guess should be close to the actual square root for faster convergence. I stop the loop when a required accuracy is reached or, failing that, after a fixed number of iterations. I keep two decimal places in the answer. The program produces the following results:

n  = 123456789.12 has solution = 11111.11
(Initial guess, Number of iterations required) = (0.1n, 15) (n/2, 18) (n, 19) (2n, 20)

n  = 0.123456789 has solution = 0.35
(Initial guess, Number of iterations required) = (0.1n, 9) (n/2, 7) (n, 6) (2n, 5)

So the best guess very much depends on the number. I'll leave it as 0.1n by default.

## Problem 8
**File:** problem8.py

**Write a program that outputs today's date and time in the format "Monday, January 10th 2019 at 1.15pm"**

Python Standard Library for datetime module: nttps://docs.python.org/3/library/datetime.html?highlight=datetime%20module#module-datetime

Python Documentation for instructions on formatting year, month day etc
strftime() and strptime() Behavior: https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-strptime-behavior

On first attempt have zero padding on day & hour, no suffix for day, and PM/AM instead of pm/am.

I used stackoverflow to get rid of leading zero in date: https://stackoverflow.com/questions/904928/python-strftime-date-without-leading-0