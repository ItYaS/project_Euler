"""             Наибольший простой делитель
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


def get_largest_prime_factor(num):
    i = 2

    while i <= num // 2:
        if num % i == 0:
            num /= i
        i += 1

    return num


if __name__ == '__main__':
    result = get_largest_prime_factor(600851475143)
    print(result)  # output: 6857
