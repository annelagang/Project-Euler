'''Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?'''
#Answer: 6857
    
import time, math
from eulertools import prime_gen
        

def solve():
    n = 600851475143
    greatest = 0
    
    for prime in prime_gen():
        if(n < prime):
            break

        if(n % prime == 0):
            greatest = prime
            n = n / prime
        else:
            continue       

    print greatest


if __name__ == '__main__':
    start = time.clock()
    solve()
    print 'Time elapsed:', (time.clock() - start)
