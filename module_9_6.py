# Генераторы
# Напишите функцию-генератор all_variants(text),
# которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.
# Пример результата выполнения программы:
# Пример работы функции:
# a = all_variants("abc")
# for i in a:
# print(i)


def all_variants(text):
    for symbol_x in range(len(text)):
        for symbol_y in range(len(text) - symbol_x):
            yield text[symbol_y:symbol_y + symbol_x + 1]


for value in all_variants("abc"):
    print(value)


# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
