def delit(n):
    dels = []  # сОЗДАЕМ СПИСОК ДЕЛИТЕЛЕЙ
    d = 1  # Начальный делитель 1
    while d * d < n:  # Начинаем от единицы и до корня этого числа
        if n % d == 0:  # Если наше число делиться на Д то
            dels.append(d)  # Добавляем само число
            dels.append(n // d)  # Добавляем деленное на число
        d += 1  # Прибавляем единицу
    if d * d == n:  # Так надо короче
        dels.append(d)
    return sorted(dels[1:-1])


def main():
    summ = 0

    for i in range(81234, 134689 + 1):
        if len(delit(i)) == 3:
            print(max(delit(i)), min(delit(i)))
    # print(set(sorted(main_list)))
    # print(summ)


if __name__ == '__main__':
    main()
