"""             Четные числа Фибоначчи
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""


def get_even_fibonacci_numbers(nums_list, fibonacci_nums_list):
    result_list = list()
    last_num = 2  # прошлое число фибоначчи
    last_index = 0  # индекс прошлого числа фибоначчи

    while True:
        if last_num >= nums_list[-1]:
            break
        last_num = int(fibonacci_nums_list[last_index]) + last_num  # сумма 2-х предыдущих чисел
        fibonacci_nums_list.append(last_num)
        last_index += 1

    for i in fibonacci_nums_list:  # отбор четных чисел
        if i % 2 == 0:
            result_list.append(i)

    return sum(result_list)


if __name__ == '__main__':
    nums = list(range(1, 4000000))
    fibonacci_nums = list([1, 2])

    result = get_even_fibonacci_numbers(nums, fibonacci_nums)
    print(result)  # output: 4613732
