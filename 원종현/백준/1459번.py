X,Y,W,S=map(int,input().split())
res=(X+Y)*W
if (X+Y)%2==0:
    res=min(res,max(X,Y)*S)
else:
    res=min(res,(max(X,Y)-1)*S+W)
res=min(res,(min(X,Y)*S)+(abs(X-Y)*W))
print(res)