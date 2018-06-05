def fibEvenSum(n):
    """Cycle through all the fibbonacci numbers starting with 1,2 and if even adding to sum. O(N)"""
    lastFib = 2
    newFib = 3
    sumEvenFib = 2

    while newFib<=n:
        newFib += lastFib
        lastFib = newFib - lastFib
#        print("newFib, lastFib",newFib, lastFib)
        if newFib %2 == 0 and newFib <= n:
            sumEvenFib += newFib

    return sumEvenFib

def main():
    print(fibEvenSum(90)) #answer 44
    print(fibEvenSum(4000000))


if __name__ == '__main__':
    if (fibEvenSum(90)==44 and fibEvenSum(4000000)==4613732):
        main()
    else:
        print("Tests Failed")
