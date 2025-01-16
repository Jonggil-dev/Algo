import sys

def func(N,idx,res):
    if idx==N:
        ans=eval(res.replace(' ',''))
        if ans==0:
            tmp.append(res)
        return
    else:
        func(N,idx+1,res+' '+str(idx+1))
        func(N,idx+1,res+'+'+str(idx+1))
        func(N,idx+1,res+'-'+str(idx+1))



for i in range(int(input())):
    N=int(input())
    tmp=[]
    func(N,1,'1')
    for a in tmp:
        print(a)
    print()