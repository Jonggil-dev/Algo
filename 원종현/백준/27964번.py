N=int(input())
S=input().split()
d={}
for i in S:
    if i not in d and i[-6:]=='Cheese':
        d[i]=1
print('yummy' if len(d)>=4 else 'sad')