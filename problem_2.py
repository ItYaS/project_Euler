"""             Четные числа Фибоначчи
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""


def get_even_fibonacci_numbers(min, max):
    result_list = list()
    fibonacci_nums_list = [1, 2]

    for i in fibonacci_nums_list:
        if i >= max:
            break
        next_num = fibonacci_nums_list[-2] + fibonacci_nums_list[-1]  # сумма 2-х предыдущих чисел
        fibonacci_nums_list.append(next_num)

    for i in fibonacci_nums_list:  # отбор четных чисел
        if i % 2 == 0:
            result_list.append(i)

    return sum(result_list)


if __name__ == '__main__':
    result = get_even_fibonacci_numbers(1, 4000000)
    print(result)  # output: 4613732
