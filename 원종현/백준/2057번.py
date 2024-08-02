N=int(input())
check=[1,1]
for i in range(2,22):
    check.append(check[i-1]*i)

res=0
for i in range(21,-1,-1):
    if res+check[i]<N:
        res+=check[i]
    elif res+check[i]==N:
        print("YES")
        break
else:
    print("NO")