N=int(input())
li=[]
li2=['' for _ in range(N)]
for i in range(N):
    s=input()
    li.append(s)
    for j in range(N):
        li2[j]+=s[j]
r1,r2=0,0
for x in range(N):
    for j in li[x].split("X"):
        if len(j)>=2:
            r1+=1
    for j in li2[x].split("X"):
        if len(j)>=2:
            r2+=1
print(r1,r2)