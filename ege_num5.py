def code(n=28):  # Вынкция выполняющая ко из задания
    n = bin(n)[2:]  # Перевод числа в двоичную систему исчисления (Строка)
    n = (8 - len(n)) * "0" + n
    # print(n)
    n = n[:-1]
    n = n[::-1]
    # print(n)
    # Пример кода для задания где надо прибавить вправо предпоследнюю и вторую ифру
    return int(n, 2)  # Возвращает число


def main():
    # Код очень зависит от задания
    k = 0
    for i in range(1, 100):
        if code(i) == i:  # Выводим то, что возвращает функция
            print(i)  # Считаем количество таких чисел
    print(k)


if __name__ == '__main__':
    # print(code(1))
    main()
