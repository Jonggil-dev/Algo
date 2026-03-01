N=int(input())
li=list(map(int,input().split()))

res=sum(li)*2+N*2+li[0]+li[-1]+sum([abs(li[i]-li[i+1]) for i in range(0,N-1)])
print(res)