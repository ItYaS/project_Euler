import math


"""             Наибольший простой делитель
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


def get_largest_prime_factor(num):
    largest_prime_factor = 0
    max_limit = math.ceil(math.sqrt(num))

    for i in range(3, max_limit):
        if num % i == 0:
            largest_prime_factor = i

    return largest_prime_factor


if __name__ == '__main__':
    result = get_largest_prime_factor(600851475143)
    print(result)  # output: 486847
