N,P,Q=map(int,input().split())
dic={}
dic[0]=1
def func(n):
    if n in dic:
        return dic[n]
    else:
        dic[n]=func(n//P)+func(n//Q)
        return dic[n]

print(func(N))