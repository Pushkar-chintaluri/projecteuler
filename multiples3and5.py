def sumofmultiples(n, upper_bound):
    """ Will return sum of all multiples of 'n' less than 'upper_bound'"""
    m = int((upper_bound-1)/n) # -- using eulers formula for sum of first 'm' natural numbers. 'm' is calculated here.
    return (n * (m*(m+1)/2))

# if sum of multiples of two separate numbers is required in an "or" rather than an "and", then subtract the sum of the multiples of the product of the two numbers
def main():
    print(sumofmultiples(3,1000)+sumofmultiples(5,1000)-sumofmultiples(15,1000))

def testcases():
    return (sumofmultiples(3,10)+sumofmultiples(5,10)==23.0 and (sumofmultiples(3,1000)+sumofmultiples(5,1000)-sumofmultiples(15,1000))==233168.0)

if __name__ == '__main__':
    if testcases():
        main()
    else:
        print("Tests Failed!")
