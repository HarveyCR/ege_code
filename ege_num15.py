def code(x, A, y): # Если y в выражение нет, его надо убрать
    f = (
            (x & 41 == 0) <= ((x & 119 != 0) <= (x & A != 0)) # Выражение, указанное в задание(Может содержать y или нет)
    )
    return f


def main():
    for A in range(100): # НАчинаем перебирать A(Иногда может быть меньше 0, обэтом будет сказанно в задании)
        ok = True # Вводим флаг
        for x in range(1000): # Перебирам X
            # for y in range(1000): # Перебираем Y(Может отсутствовать)
                if not code(x, A, 0): # отправляем в функцию и проверяем, выводит ли True, если нет, опускаем флаг
                    ok = False # Опускаем флаг
        if ok: # Если после дого, как от прошел весь x и всегда был True, мы нашли нужное число.
            print(A) # Выводим его


if __name__ == '__main__':
    main()