N=int(input())
r=set()
for i in range(N):
    s=input()
    t=[]
    for i in s:
        t.append(ord(i))
    t=tuple(sorted(t))
    r.add(t)
print(len(r))