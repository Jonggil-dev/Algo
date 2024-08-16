a=int(input())
t=int(input())
x=int(input())
li=[]
bun=degi=1
n=0
while True:
    prev_n=bun
    n+=1
    for _ in range(2):
        li.append((bun,0))
        bun+=1
        li.append((degi,1))
        degi+=1
    for _ in range(n+1):
        li.append((bun,0))
        bun+=1
    for _ in range(n+1):
        li.append((degi,1))
        degi+=1
    if prev_n<t<=bun:
        print(li.index((t,x))%a)
        break
