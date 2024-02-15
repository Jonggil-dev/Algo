N=int(input())
li=list(map(int,input().split()))
li.sort()
s=set()

r=1
for i in li:
    if r<i:
        break
    r+=i
print(r)