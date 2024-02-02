X=input()
r=0
while len(X)>1:
    r+=1
    X=str(sum([int(i) for i in X]))
print(r)
print("NO" if int(X)%3 else "YES")