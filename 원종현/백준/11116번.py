for _ in range(int(input())):
    M=int(input())
    l=list(map(int,input().split()))
    r=sorted(list(map(int,input().split())),reverse=True)
    while r:
        now=r.pop()
        if now+1000 in l:
            r.pop(r.index(now+500))
            l.pop(l.index(now+1000))
            l.pop(l.index(now+1500))
    print(len(l)//2)