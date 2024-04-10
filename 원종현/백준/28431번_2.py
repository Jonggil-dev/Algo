d={}
for i in range(5):
    n=int(input())
    if n in d:
        del d[n]
    else:
        d[n]=1
for i in d.keys():
    print(i)