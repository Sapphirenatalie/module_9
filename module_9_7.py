# Декораторы

# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three).
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.

# Пример:
# result = sum_three(2, 3, 6)
# print(result)


def is_prime(func):
    def wrapper(*numbers):
        summation = func(*numbers)
        count = 0
        for element in range(1, summation + 1):
            if summation % element == 0:
                count += 1
        if count > 2:
            return f'Составное \n{summation}'
        if count == 2:
            return f'Простое \n{summation}'

    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11
