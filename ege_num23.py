def calc(begin, end):
    if begin > end or begin == 15:
        return 0
    if begin == end:
        return 1
    # if begin % 2 == 0:
    #     return calc(begin + 1, end) + calc(2 * begin + 1, end)
    # else:
    return calc(begin + 1, end)


def main():
    print(calc(1, 25)) # Вызываем функцию калькулятор, от a до b


if __name__ == '__main__':
    main()
