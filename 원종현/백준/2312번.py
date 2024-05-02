import sys
input=sys.stdin.readline
def func(N):
    prime=[]
    for i in range(2,N+1):
        tmp=0
        while N%i==0:
            tmp+=1
            N=N//i
        if tmp:
            prime.append([i,tmp])
    for i in prime:
        print(*i)

T=int(input())
for _ in range(T):
    func(int(input()))