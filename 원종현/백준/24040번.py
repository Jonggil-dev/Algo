import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    if N%9==0 or N%3==2:
        print('TAK')
    else:
        print('NIE')