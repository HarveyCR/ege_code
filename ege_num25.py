def main():
    f = open("26-89.txt")
    # count = f.readline()
    # sp = sorted([int(x) for x in f.readlines()])[::-1]
    # print(sp)
    #
    # k = 1
    # for i in range(count):
    #     if sp[i + 1] - sp[i] >= 3:
    #         k += 1
    # print(k)
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
    a.sort(reverse=True)
    gift = [a[0]]
    for i in range(n):
        if gift[-1] - a[i] >= 3:
            gift.append(a[i])
    print(len(gift), gift[-1])


if __name__ == '__main__':
    main()
