import math

def is_even(n):
    return n % 2 == 0


def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def is_prime(n):
    # n**0.5 == math.sqrt(n)
    n = abs(n)
    for x in range(2, int(n**0.5 + 1)):
        if n % x == 0:
            return False
    return True


def nth(gen, n):
    '''Returns nth number from a given generator.'''
    for i in xrange(n - 1):
        gen.next()
    return gen.next()


#source: http://www.siafoo.net/snippet/145
def is_triangle(n):
    x = (math.sqrt(8*n + 1) - 1) / 2
    if x - int(x) > 0: # if x is not an integer
        return False
    return int(x)


def prime_gen():
    yield 2
    yield 3
    i = 5
    while True:
        if is_prime(i):
            yield i
        i += 2
        

def fib_gen():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

        
def triangle_num_gen(n = 1):
    while True:
        yield n * (n + 1) / 2
        n += 1


#using Binet's formula
#source: http://en.literateprograms.org/Fibonacci_numbers_(Python)#Recursion_with_memoization
def fib(n):
    return int(round((phi**n - (1-phi)**n) / 5**0.5))


#source: http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
#author: Piet Delport
def primes_sieve(limit):
    a = [True] * limit                      # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i, limit, i):   # Mark factors non-prime
                a[n] = False


#source: http://blog.dhananjaynene.com/2009/01/2009-is-not-a-prime-number-a-python-program-to-compute-factors/
def prime_factors(n):
  #yield 1
  i = 2
  limit = n**0.5
  while i <= limit:
    if n % i == 0:
      yield i
      n = n / i
      limit = n**0.5
    else:
      i += 1
  if n > 1:
    yield n
    

from collections import Counter
def gcm(num1, num2):
    gcm = list((Counter([x for x in prime_factors(num1)])
                & Counter([x for x in prime_factors(num2)])).elements())

    return reduce(lambda prod1, prod2: prod1 * prod2, gcm)

    
def factor_count_dict(prime_factors):
    '''Returns a dictionary mapping of the prime factors of a number and
it's frequency.'''
    dict_factor_count = {}
    for prime in prime_factors:
        dict_factor_count[prime] = dict_factor_count.get(prime,0) + 1

    return dict_factor_count


#formula: (a+1)*(b+1)*...(k+1)
#source: http://www.manhattangmat.com/forums/is-there-a-formula-to-calculate-the-number-of-factors-t2500.html
#author: David Pollack
def factor_count(dict_factor_list):
    dict = factor_count_dict(dict_factor_list)

    total_count = 1

    for count in dict.values():
        total_count *= count + 1

    return total_count


#formula: (n / 10) + (n % 10) * 100000
#source: http://projecteuler.net/thread=35;page=2
#author: jorgbrown
def rotate_digits(n):
    num = n
    count = len(str(num))
    power = count - 1

    rotated = [num]
    #start at 1 to avoid rotating back to the given num 
    ctr = 1
    while ctr < count:
        num = (num / 10) + (num % 10) * (10 ** power)
        rotated.append(num)
        ctr += 1        

    #return distinct (esp for 11)
    return set(rotated)


def break_into_digits(n):
    '''Returns the digits of a base 10 number.'''
    count = len(str(n))
    power = count - 1

    digits = []
    ctr = 0
    while ctr < count:
        num = n / (10 ** power)
        if ctr != 0:
            num = num % 10
            
        digits.append(num)
        power -= 1
        ctr += 1

    return digits


#source: http://stackoverflow.com/questions/1408823/int-and-string-parsing
#author: Charles Ma
#modified to be a generator
def extract_digits_reversed(num):
    while num > 0:
        yield num % 10
        num /= 10


def collatz_gen(num):
    n = num
    yield n
    while n != 1:
        if is_even(n):
            n = n / 2
        else:
            n = 3 * n + 1

        yield n


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
