
from const import EXPANSION_LIMIT
from util import factorial


def cosine(n: int):

    for i in range(EXPANSION_LIMIT):
        sign = 1 if not i % 2 else -1
        yield sign * (n**(2 * i)) / factorial(2 * i)

if __name__ == '__main__':
    cos = list(cosine(0.3))
    print(cos)