N=int(input())

res=1
for i in range(2,N+1):
    res*=i
    while True:
        if str(res)[-1]=='0':
            res//=10
        else:
            break
    res%=100000000000000000
print(str(res)[-5:])