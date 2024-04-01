import sys
input=sys.stdin.readline
N,M=map(int,input().split())
li=[0]+list(map(int,input().split()))+[0]
r=0
for i in range(1,N):
    if li[i] and not li[i-1]:
        r+=1
for i in range(M):
    s=input().split()
    if s[0]=='0':
        print(r)
    else:
        if li[int(s[1])]==1:
            continue
        else:
            if li[int(s[1])-1]==0 and li[int(s[1])+1]==0:
                r+=1
            elif li[int(s[1])-1]==1 and li[int(s[1])+1]==1:
                r-=1
            li[int(s[1])]=1

