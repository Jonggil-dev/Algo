import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
res=0

def func(st,end):
    global res
    if st<end:
        mid=(st+end)//2
        func(st,mid)
        func(mid+1,end)
        tmp=[]
        x,y=st,mid+1
        while x<=mid and y<=end:
            if li[x]<=li[y]:
                tmp.append(li[x])
                x+=1
            else:
                tmp.append(li[y])
                y+=1
                res+=(mid-x)+1
        if x<=mid:
            tmp+=li[x:mid+1]
        if y<=end:
            tmp+=li[y:end+1]
        for i in range(len(tmp)):
            li[st+i]=tmp[i]
func(0,N-1)
print(res)