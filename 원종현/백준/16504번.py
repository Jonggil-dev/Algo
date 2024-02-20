N=int(input())
li=sum([sum(list(map(int,input().split()))) for _ in range(N)])
print(li)
