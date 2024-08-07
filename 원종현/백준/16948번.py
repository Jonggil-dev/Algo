N,S,E=map(int,input().split())
r=0
while S!=E:
    S-=S//2
    E-=E//2
    r+=1
print(r)