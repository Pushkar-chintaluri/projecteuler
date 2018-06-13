def sum_of_squares(num):
    """ Using formula: (n)(n+1)(2n+1)/6 """
    return (num * (num+1) * (2*num + 1))/6

def square_of_sum(num) :
    """ Using formula: (n)(n+1)/2 """
    return ((num * (num+1))/2)**2

def sum_square_diff(num):
    return square_of_sum(num) - sum_of_squares(num)


