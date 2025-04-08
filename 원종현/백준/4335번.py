import sys
input=sys.stdin.readline
while True:
    ma,mi=10,1
    res=''
    while True:
        N=int(input())
        if N==0:
            break
        tmp=input().rstrip()
        if tmp=='right on':
            if N>=mi and N<=ma:
                res='Stan may be honest'
            else:
                res='Stan is dishonest'
            break
        elif tmp=='too high':
            ma=min(ma,N-1)
        elif tmp=='too low':
            mi=max(mi,N+1)
    if N==0:
        break
    print(res)