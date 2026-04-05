X,K=map(int,input().split())
res=''
X,K=list(bin(X)[2:]),list(bin(K)[2:])

while K:
    if X:
        now=X.pop()
        if now=='1':
            res+='0'
        else:
            res+=K.pop()
    else:
        res+=K.pop()
print(int(res[::-1],2))