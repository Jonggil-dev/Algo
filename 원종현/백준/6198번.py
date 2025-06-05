li=[]
for i in range(int(input())):
    li.append(int(input()))
stk=[]
res=0


for i in li:
    while stk and stk[-1]<=i:
        stk.pop()
    stk.append(i)
    res+=len(stk)-1
print(res)