'''Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''
#Answer: 233168


import time

def solve():
    limit = 1000
    sum = 0

    nums = xrange(1, limit)

    ##for num in nums:
    ##    if(num % 3 == 0) or (num % 5 == 0):
    ##        sum = sum + num
                
    ##print sum

    #predicate
    def isMultiple(num, multiples):
        for multiple in multiples:
            if(num % multiple == 0):
                return True
        return False

    multiples = [3,5]

    for num in nums:
        if(isMultiple(num, multiples)):
            sum = sum + num

    return sum


if __name__ == '__main__':
    start = time.clock()
    print 'Answer:', solve()
    print 'Time elapsed:', (time.clock() - start)

    
