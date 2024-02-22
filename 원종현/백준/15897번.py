n=int(input())-1
ans=0
i=n+1
while i!=0:
    next_i=n//((n//i)+1)
    ans+=(n//i+1)*(i-next_i)
    i=next_i
print(ans)