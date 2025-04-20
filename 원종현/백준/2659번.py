li=list(map(int,input().split()))

def func(N):
    tmp=int(''.join(map(str,N)))
    for i in range(1,4):
        r=int(''.join(map(str,N[i:]+N[:i])))
        if tmp>r:
            tmp=r
    return tmp
res=func(li)
cnt=1
for i in range(1111,res):
    if '0' not in list(str(i)) and i==func(list(map(int,str(i)))):
        cnt+=1
print(cnt)