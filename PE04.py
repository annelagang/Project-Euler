'''Problem 4
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''
#Answer: 906609


import time
from eulertools import is_palindrome

        
def solve():
    first_half = range(900, 951)
    second_half = range(951, 1000)

    palindrome = []
    prod = 0
    for first in first_half:
        for second in second_half:
            prod = first * second
            if(is_palindrome(str(prod))):
                    palindrome.append(prod)
                
    for prod_palindrome in palindrome:
        prod_str = str(prod_palindrome)
        if(prod_str[0] == '9'):
            print prod_palindrome
            break


if __name__ == '__main__':
    start = time.clock()
    solve()
    print 'Time elapsed:', (time.clock() - start)

    
