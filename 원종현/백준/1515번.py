S=input()
res=0
idx=0
while True:
    res+=1
    for i in str(res):
        if S[idx]==i:
            idx+=1
            if idx>=len(S):
                print(res)
                exit()