N=int(input())
li1=sorted(list(map(int,input().split())),reverse=True)
li2=sorted(list(map(int,input().split())))
cnt=0
for i in li1:
    if i<li2[-1]:
        cnt+=1
        li2.pop()

print("YES" if cnt>=(N+1)/2 else "NO")