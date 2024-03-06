def convert_to(num, count):
    new_num = ''
    while num > 0:
        new_num += str(num % count)
        num //= count
    return new_num[::-1]


def main():
    # convert_to(12345, 8)
    print(bin(int("F2E", 16))[2:])
    k = 0
    for i in range(18, 167):
        k += 1
    print(k)


if __name__ == '__main__':
    main()
