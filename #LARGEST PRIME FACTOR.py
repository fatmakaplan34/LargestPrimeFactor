#LARGEST PRIME FACTOR
#In this code we'll find the largest prime factor of number n.
#n have to be a positive integer and i choosed the number 55674892404850 as an example.
#I choosed this number because it has a lot of prime factors and it's a big number so you can see the efficiency of the code.

def largest_prime_factor(n):
    value=2
    largest=0
    while n>1:
        if n%value==0:
            largest=value
            n//=value

        else:
            value+= 1

    return largest
n=55674892404850
result=largest_prime_factor(n)
print(f"Largest prime factor of {n} is {result}.")

#Also you can use the following code to find the largest prime factor of a number.
#This code is more efficient that the previous one.
#If you want to see all of the prime factors of a number you can remove the "max" function from the code.

import math 
from sympy import primefactors
n=55674892404850
print(max(primefactors(n)))