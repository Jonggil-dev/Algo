t=0
d={}
t=[]
for i in range(1,9):
    tmp=int(input())
    d[tmp]=i
    t.append(tmp)
t.sort()
print(sum(t[3:]))
r=[]
for i in range(3,8):
    r.append(d[t[i]])
print(*sorted(r))