a,b=map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))
res=A-B
res=sorted(list(res))
print(len(res))
if res:
    print(*res)