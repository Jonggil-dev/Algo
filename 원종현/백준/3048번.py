A,B=map(int,input().split())
a1=list(input())
b1=list(input())
t=int(input())
a1.reverse()
res=a1+b1
for _ in range(t):
    for i in range(len(res)-1):
        if res[i] in a1 and res[i+1] in b1:
            res[i],res[i+1]=res[i+1],res[i]
            if res[i+1]==a1[-1]:
                break
print(''.join(res))