S=input()
P=input()

idx,res=0,0

while idx<len(P):
    val,tmp,tmp_idx=0,0,0
    while tmp_idx<len(S) and idx+tmp<len(P):
        if P[idx+tmp]==S[tmp_idx]:
            tmp+=1
            val=max(val,tmp)
        else:
            tmp=0
        tmp_idx+=1
    idx+=val
    res+=1
print(res)