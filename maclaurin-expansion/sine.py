
# from . import sin, factorial, EXPANSION_LIMIT
from util import factorial
from const import EXPANSION_LIMIT


# SIGMA i=0, n  =>  f(i)



def sin(x):

    total = 0

    for i in range(0, EXPANSION_LIMIT):
        sign_b = i % 2 == 0

        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        total += sign_b * term
        print('total - ', total)
    return total


if __name__ == '__main__':
    sin(0.3)
