N=input()
cnt=0
max_val,min_val='',''
for i in N:
    if i=='K':
        if cnt>0:
            max_val+=str(5*10**cnt)
            min_val+=str(1*10**cnt+5)
            cnt=0
        else:
            max_val+='5'
            min_val+='5'
    else:
        cnt+=1
if cnt>0:
    max_val+='1'*cnt
    min_val+=str(1*10**(cnt-1))
print(max_val)
print(min_val)