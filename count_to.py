def convert_to(num, count):
    new_num = ''
    while num > 0:
        new_num += str(num % count)
        num //= count
    return new_num[::-1]


def main():
    convert_to("12345", 8)


if __name__ == '__main__':
    main()
