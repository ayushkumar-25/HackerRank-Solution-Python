if __name__ == '__main__':
    d = {}
    l = []
    final = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
        l.append(score)
    l.sort()
    a = l[0]
    for i in range(len(l)):
        if a in l:
            l.remove(a)
    for k, v in d.items():
        if v == l[0]:
            final.append(k)
    final.sort()
    for i in range(len(final)):
        print(final[i])
