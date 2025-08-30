import sys,itertools
input=sys.stdin.readline
def func(t):
    l=[]
    cnt=0
    tmp=0
    for i in t:
        cnt+=i
        l.append(cnt)
    for i in range(0,len(l)-1):
        for t in range(i+1,len(l)):
            if l[i]+50==l[t]:
                tmp+=1
    return tmp
res=0
N=int(input())
li=list(map(int,input().split()))
li.sort()
if max(li)>50:
    print(0)
else:
    tli=list(itertools.permutations(li))
    for i in tli:
        c=func(list(i))
        if c>res:
            res=c
    print(res)