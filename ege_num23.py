def calc(begin, end, pos):  # Функция калькулятор
    if begin > end:  # Если начальная точка стала больше чем конец, возвращаем 0
        return 0
    if begin == end:
        if pos == 1:  # Если начальная точка стала равна концу, возвращаем 0
            return 1
        return 0
    # if begin % 2 == 0:
    #     return calc(begin + 1, end) + calc(2 * begin + 1, end)
    # else:
    return calc(begin + 1, end, 1) + calc(begin * 2, end,
                                          0)  # Возвращаем рекурсию, каждый вызов это операция проводимая по условию


def main():
    print(calc(5, 32, 2))  # Вызываем функцию калькулятор, от a до b


if __name__ == '__main__':
    main()
