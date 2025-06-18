N=int(input())
li=list(input().split())
def sort(li):
    for i in range(len(li)-1,0,-1):
        for j in range(i):
            if int(li[j]+li[j+1])<int(li[j+1]+li[j]):
                li[j],li[j+1]=li[j+1],li[j]
sort(li)
res=''
for i in li:
    res+=i
print(str(int(res)))
print(res)