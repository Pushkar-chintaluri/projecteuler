import math
import pdb

def is_prime(num):

    """ Helper function that checks if a number is prime or not"""

    for n in range(2,int(math.sqrt(num))+1):
        if num%n == 0:
            return False
    return True

def largest_prime_factor(num):
    """ Brute Force solution """

#    pdb.set_trace()
    primesDict = {1:True,2:True,3:True,4:False,5:True}
    n = 2
    factor = 0
    while num>1:
        if not primesDict.has_key(n):
            primesDict[n]=is_prime(n)

        if primesDict[n]:
            if num%n == 0:
                factor = n
                num = num/n
                n = 2
            else:
                n += 1
        else:
            n += 1

    return factor


def main():
    if largest_prime_factor(42)==7 and largest_prime_factor(13195)==29 and largest_prime_factor(600851475143)==6857:
        print("Tests Passed")
    else:
        print("Oops, something broke")

if __name__ == "__main__":
    main()
