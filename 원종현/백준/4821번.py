import sys
input=sys.stdin.readline

while True:
    N=int(input())
    if N==0:
        break
    li=[0]*(N+1)
    S=input().rstrip().split(',')
    for i in S:
        st,end=(int(i),int(i)) if '-' not in i else map(int,i.split('-'))
        if st>end:
            continue
        for j in range(st,end+1):
            if 0<=j<=N:
                li[j]=1
    print(sum(li))