def game(k1, k2, pos):  # Функция игры
    # дальше три проверки
    if k1 + k2 >= 68 and (pos == 2 or pos == 4):  # Если сейчас нужный нам Ход и уловия Выигрыша выполены, то возврашаем True
        return True
    if k1 + k2 < 68 and pos == 4:  # Если сейчас нужный нам Ход, но уловия Выигрыша не выполены, то возврашаем False
        return False
    if k1 + k2 >= 68 and pos != 4:  # Если уловия Выигрыша выполены, но не нужный нам Ход, то возврашаем False
        return False
    # Далше количество if равно количеству ходов в игре

    if pos == 0:  # Первый ход
        return game(k1 + 1, k2, pos + 1) and game(k1 + k2, k2, pos + 1) and game(k1, k2 + 1, pos + 1) and game(k1, k2 + k1,
                                                                                                            pos + 1)
    if pos == 1:  # Второй ход
        return game(k1 + 1, k2, pos + 1) or game(k1 + k2, k2, pos + 1) or game(k1, k2 + 1, pos + 1) or game(k1,
                                                                                                               k2 + k1,
                                                                                                               pos + 1)
    if pos == 2:  # Первый ход
        return game(k1 + 1, k2, pos + 1) and game(k1 + k2, k2, pos + 1) and game(k1, k2 + 1, pos + 1) and game(k1, k2 + k1,
                                                                                                            pos + 1)
    if pos == 3:  # Первый ход
        return game(k1 + 1, k2, pos + 1) or game(k1 + k2, k2, pos + 1) or game(k1, k2 + 1, pos + 1) or game(k1, k2 + k1,
                                                                                                            pos + 1)

def main():
    for i in range(1, 59):
        if game(8, i, 0):  # Выфункцию игры, k1, k2 - куоличество камней в кучах. pos - ход, в начале 0
            print(i)


if __name__ == '__main__':
    main()
