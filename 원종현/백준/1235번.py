import sys
input=sys.stdin.readline
N=int(input())
res=0
s=[input().rstrip()[::-1] for i in range(N)]
for i in range(1,len(s[0])+1):
    tmp=list(map(lambda x:x[:i],s))
    if len(tmp) == len(set(tmp)):
        print(i)
        break
