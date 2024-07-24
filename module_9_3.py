# Генераторные сборки
# Дано 2 списка:
# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']
# Необходимо создать 2 генераторных сборки:
# В переменную first_result запишите генераторную сборку,
# которая высчитывает разницу длин строк из списков first и second,
# если их длины не равны.
# Для перебора строк попарно из двух списков используйте функцию zip.
# В переменную second_result запишите генераторную сборку,
# которая содержит результаты сравнения строк в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip.
# Используйте функции range и len.

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = ((len(item1) - len(item2)) for item1, item2 in zip(first, second) if len(item1) != len(item2))

print(list(first_result))

second_result = (len(first[item1]) == len(second[item2]) for item1 in range(len(first))
                 for item2 in range(len(second)) if item1 == item2)

print(list(second_result))

# Пример результата выполнения программы:
# Пример выполнения кода:
# print(list(first_result))
# print(list(second_result))

# Вывод в консоль:
# [1, 2]
# [False, False, True]
