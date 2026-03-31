A=int(input())

a=list('0'+bin(A)[2:])
for i in range(len(a)-1,0,-1):
    if a[i-1]=='1'and a[i]=='0':
        a[i-1],a[i]='0','1'
        a[i+1:]=sorted(a[i+1:],reverse=True)
        break

b=list('0'+bin(A)[2:])
for i in range(len(b)-1,0,-1):
    if b[i-1]=='0'and b[i]=='1':
        b[i-1],b[i]='1','0'
        b[i+1:]=sorted(b[i+1:])
        break

print(int(''.join(a),2) if int(''.join(a),2)!=A else 0,int(''.join(b),2))