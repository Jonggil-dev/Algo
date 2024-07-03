import sys

input=sys.stdin.readline
T=int(input())
for _ in range(T):
    s=list(input().rstrip())
    i,j=0,1
    for idx in range(1,len(s)):
        if s[idx]>s[idx-1] and i<idx:
            i=idx
    for idx in range(1,len(s)):
        if s[idx]>s[i-1] and j<idx:
            j=idx
    if i!=0 and j!=0:
        s[i-1],s[j]=s[j],s[i-1]
        s[i:]=list(reversed(s[i:]))
    print(''.join(s))