N,K=map(int,input().split())
st=0
digit=1
nine=9
while K>nine*digit:
    K-=digit*nine
    st+=nine
    nine*=10
    digit+=1
res=st+1+(K-1)//digit
print(-1 if res>N else str(res)[(K-1)%digit])