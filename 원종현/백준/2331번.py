A,P=map(int,input().split())
tmp=0
li=[A]
while True:
    tmp=0
    for i in str(li[-1]):
        tmp+=int(i)**P
    if tmp in li:
        break

    li.append(tmp)
print(li.index(tmp))