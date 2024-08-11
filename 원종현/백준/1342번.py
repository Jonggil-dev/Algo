import sys
input=sys.stdin.readline


def func(x,y):
    if y==len(li):
        return 1
    tmp=0
    for i in dic.keys():
        if x==i or dic[i]==0:
            continue
        dic[i]-=1
        tmp+=func(i,y+1)
        dic[i]+=1
    return tmp


li=list(input().strip())
dic=dict()
for i in li:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
res=func('',0)
print(res)