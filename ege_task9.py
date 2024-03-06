def main():
    file = open('9-170.txt')

    k = 0
    for s in file:
        sp = [int(x) for x in s.split()]
        if len(sp) - len(set(sp)) == 1:
            spp = []
            snp = []
            for i in range(len(sp)):
                if sp.count(sp[i]) == 2:
                    spp.append(sp[i])
                else:
                    snp.append(sp[i])
            # print(spp, snp)
            if max(snp) + min(snp) <= sum(spp):
                k += 1
    print(k)


if __name__ == '__main__':
    main()
