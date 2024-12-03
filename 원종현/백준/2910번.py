N,C=map(int,input().split())
li=list(map(int,input().split()))
dic={}
idx=1
res=''
for i in li:
    if i in dic:
        dic[i][0]+=1
    else:
        dic[i]=[1,idx]
        idx+=1

dic2=sorted(dic.items(), key=lambda x:[-x[1][0],x[1][1]])

for k,v in dic2:
    res+=(str(k)+' ')*v[0]
print(res[:-1])