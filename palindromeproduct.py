def is_palindrome(num):
    """ Takes a number or string and returns true if it is a palindrome """
    return str(num) == str(num)[-1::-1]


def palin_prod(lower=100, upper=1000):
    """ Brute force solution, O(N^2) time complexity"""
    prod = 0
    for i in range(lower, upper):
        for j in range(lower,upper):
            cand = i*j
            if is_palindrome(cand):
                if (cand)>prod:
                    prod = cand

    return prod
