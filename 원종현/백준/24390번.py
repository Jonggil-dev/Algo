M,S=map(lambda x:int(x),input().split(':'))
print(M,S)
res=1+(M//10+M%10)
if S>=30:
    res+=(S-30)//10
else:
    res+=S//10
print(res)
