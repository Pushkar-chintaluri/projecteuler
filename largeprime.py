from largestprimefactor import *

def prime_sequence(length):
    """ Not storing the primes, but looking at only odd numbers until 10001 primes are found """
    prime_candidate = 15
    prime_ctr = 6
    while prime_ctr < length:
        if is_prime(prime_candidate):
            prime_ctr += 1
        prime_candidate+=2 # Note that this will add 2 to the final result...

    return prime_candidate-2
            

