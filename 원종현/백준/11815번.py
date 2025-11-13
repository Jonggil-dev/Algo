N=int(input())
li=list(map(int,input().split()))

for i in li:
    print(1 if i==int(i**0.5)**2 else 0,end=" ")