import sys
input=sys.stdin.readline
N=int(input())
le,ri=input().rstrip().split('*')
for _ in range(N):
    now=input().rstrip()
    if len(now)>=len(le+ri):
        if le==now[:len(le)] and ri==now[-len(ri):]:
            print('DA')
        else:
            print('NE')
    else:
        print('NE')