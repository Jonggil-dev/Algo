import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    b,w=0,0
    l1,l2=input(),input()
    for i in range(N):
        if l1[i]!=l2[i]:
            if l1[i]=='B':
                b+=1
            else:
                w+=1
    print(max(b,w))