while True:
    S=input()
    if S=='#':
        break
    S1,S2=S.split()
    res=[0,0,0]
    flag1=[1]*(len(S1))
    flag2=[1]*(len(S1))
    for i in range(len(S1)):
        if S1[i]==S2[i]:
            res[0]+=1
            flag1[i]=0
            flag2[i]=0
    for i in range(len(S1)):
        if flag1[i]:
            if i>0 and S1[i]==S2[i-1] and flag2[i-1]:
                flag2[i-1]=0
            elif i<len(S1)-1 and S1[i]==S2[i+1] and flag2[i+1]:
                flag2[i+1]=0
            else:
                continue
            res[1]+=1
            flag1[i]=0
    for i in range(len(S1)):
        if flag1[i]:
            for j in range(len(S1)):
                if S1[i]==S2[j] and flag2[j]:
                    res[2]+=1
                    flag1[i]=0
                    flag2[j]=0
                    break
    print(f'{S2}: {res[0]} black, {res[1]} grey, {res[2]} white')