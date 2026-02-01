import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    M=int(input())
    li=[]
    for i in range((M-1)//10+1):
        li.extend(list(map(int,input().split())))
    s=[li[0]]
    for i in range(1,M):
        s.append(s[-1]+li[i])
    s=set(s)
    max_s=max(s)
    cand=[]
    for i in range(1,int(max_s**0.5)+1):
        if max_s%i!=0:
            continue
        if i>=max(li):
            cand.append(i)
        if i**2!=max_s:
            cand.append(max_s//i)
    cand.sort()
    res=0
    print(cand)
    for i in cand:
        x=max_s//i
        for j in range(1,x+1):
            if i*j not in s:
                break
        else:
            res=i
        if res:
            print(res)
            break
