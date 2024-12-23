import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    N,M,K=map(int,input().split())
    if max(N,M)<K*2:
        print("Yuto")
    else:
        print("Yuto" if N*M%2 else"Platina")