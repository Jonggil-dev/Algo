r="Valid"

now=input()
start=now
c1="ABCDEF"
c2="123456"
check=set()
for i in c1:
    for j in c2:
        check.add(i+j)

check.remove(now)
for i in range(35):
    next=input()
    if abs(ord(now[0])-ord(next[0]))+abs(ord(now[1])-ord(next[1]))!=3 or (abs(ord(now[0])-ord(next[0]))==3 or abs(ord(now[1])-ord(next[1]))==3):
        r="Invalid"
        break
    now=next
    if now in check:
        check.remove(now)
    else:
        r="Invalid"
        break
if abs(ord(now[0])-ord(start[0]))+abs(ord(now[1])-ord(start[1]))!=3 or (abs(ord(now[0])-ord(start[0]))==3 or abs(ord(now[1])-ord(start[1]))==3):
    r="Invalid"
print(r)