N=int(input())

def custom_sort(inputs):
    res=0
    for i in inputs:
        if i.isdigit():
            res+=int(i)
    return res
li=[]
for i in range(N):
    li.append(input())

li.sort(key = lambda x:(len(x),custom_sort(x),x))

print(*li,sep="\n")