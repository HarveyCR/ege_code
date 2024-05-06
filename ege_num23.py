def calc(begin, end):  # Функция калькулятор
    if begin > end:  # Если начальная точка стала больше чем конец, возвращаем 0
        return 0
    if begin == end:
        return 1
    # if begin % 2 == 0:
    #     return calc(begin + 1, end) + calc(2 * begin + 1, end)
    # else:
    return calc(begin + 1, end) + calc(begin + 3, end,) + calc(begin * 4, end)  # Возвращаем рекурсию, каждый вызов это операция проводимая по условию


def main():
    print(calc(1,18))  # Вызываем функцию калькулятор, от a до b


if __name__ == '__main__':
    main()
