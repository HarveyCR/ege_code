from count_to import convert_to


# Задача имеет два основных типа, когда считает программа, и когда надо считать руками
# Пример кода когда надо считать руками
# Эти Задачи нужны, когда основание системы исчислении больше 10 и не 16
def main():
    for x in range(13):
        a1 = 1 * 13 ** 0 + 2 * 13 ** 1 + 1 * 13 ** 2 + x * 13 ** 3 + 8 * 13 ** 4  # Тут показан пример, Как число 8x121(где X любое число от 0 до 12) в системи исчисления 13 перевести в 10ую,
        a2 = 5 * 13 ** 0 + 7 * 13 ** 1 + 5 * 13 ** 2 + x * 13 ** 3 + 7 * 13 ** 4  # Тут показан пример, Как число 7x575(где X любое число от 0 до 12) в системи исчисления 13 перевести в 10ую
        # print(a1, a2)  # Выводим два числа
        if (a1 - a2) % 19 == 0:  # Проверяем на условие, данное в задание
            print(x, (a1 - a2) / 19)  # Выводим X нужное нам число и деление его разности на 19(по условию)


if __name__ == '__main__':
    main()
