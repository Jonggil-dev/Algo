N=int(input())
li=[int(input()) for _ in range(N)]
li.sort(reverse=True)
res=0
for i in range(2,len(li),3):
    res+=li[i]
print(sum(li)-res)