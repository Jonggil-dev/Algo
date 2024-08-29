def check(word,st,end,cnt):
    global res
    if cnt>2:
        return 0
    while st<end:
        if word[st]==word[end]:
            st+=1
            end-=1
        else:
            check(word,st+1,end,cnt+1)
            check(word,st,end-1,cnt+1)
            return
    res=min(res,cnt)

for i in range(int(input())):
    s=input()
    res=2
    check(s,0,len(s)-1,0)
    print(res)