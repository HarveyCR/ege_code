def game(k1, k2, pos):
    if k1 + k2 >= 79 and (pos == 4 or pos == 2):
        return True
    if k1 + k2 < 79 and pos == 4:
        return False
    if k1 + k2 >= 79 and pos != 4:
        return False
    if pos == 0:
        return game(k1 + 3, k2, pos + 1) and game(k1 * 2, k2, pos + 1) and game(k1, k2 + 3, pos + 1) and game(k1,
                                                                                                              k2 * 2,
                                                                                                              pos + 1)
    if pos == 1:
        return game(k1 + 3, k2, pos + 1) or game(k1 * 2, k2, pos + 1) or game(k1, k2 + 3, pos + 1) or game(k1, k2 * 2,
                                                                                                           pos + 1)
    if pos == 2:
        return game(k1 + 3, k2, pos + 1) and game(k1 * 2, k2, pos + 1) and game(k1, k2 + 3, pos + 1) and game(k1,
                                                                                                              k2 * 2,
                                                                                                              pos + 1)
    if pos == 3:
        return game(k1 + 3, k2, pos + 1) or game(k1 * 2, k2, pos + 1) or game(k1, k2 + 3, pos + 1) or game(k1, k2 * 2,
                                                                                                           pos + 1)


def main():
    for i in range(1, 69):
        if game(9, i, 0):
            print(i)


if __name__ == '__main__':
    main()
