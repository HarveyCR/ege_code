def main():
    f = open('24-j5.txt', 'r')
    s = f.read()
    k = 0
    for i in range(len(s) - 3):
        if s[i:i + 5] != "STOCK" and s[i + 2:i + 5] == "OCK":
            k += 1
    print(k)


if __name__ == '__main__':
    main()
