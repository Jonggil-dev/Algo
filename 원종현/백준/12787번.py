import sys
input=sys.stdin.readline

for i in range(int(input())):
    M,N=input().split()
    res=''
    if M=='1':
        ip=list(map(int,N.split('.')))
        for j in ip:
            res+=bin(j)[2:].zfill(8)
        print(int(res,2))
    else:
        ip=str(bin(int(N))[2:]).zfill(64)
        for j in range(8):
            res+=str(int(ip[j*8:(j+1)*8],2))
            if j!=7:
                res+='.'
        print(res)