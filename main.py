if __name__ == '__main__':
    lst = list()
    n = int(input())
    for _ in range(n):
        s = input()
        if s.startswith("insert"):
            s = s.strip().split()
            lst.insert(int(s[1]), int(s[2]))
        elif s.startswith("remove"):
            s = s.strip().split()
            lst.remove(int(s[1]))
        elif s.startswith("append"):
            s = s.strip().split()
            lst.append(int(s[1]))
        elif s.startswith("sort"):
            lst.sort()
        elif s.startswith("pop"):
            lst.pop()
        elif s.startswith("reverse"):
            lst.reverse()
        elif s.startswith("print"):
            print(lst)
