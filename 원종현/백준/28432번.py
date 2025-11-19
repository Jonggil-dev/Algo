N=int(input())
li=[]
for i in range(N):
    li.append(input())

M=int(input())
tmp=[]
for i in range(M):
    tmp.append(input())

if '?' in li:
    idx=li.index('?')
    if idx==0:
        st=''
    else:
        st=li[idx-1][-1]
    if idx==len(li)-1:
        end=''
    else:
        end=li[idx+1][0]
    for word in tmp:
        if word not in li:
            if (not st or word[0]==st) and (not end or word[-1]==end):
                print(word)