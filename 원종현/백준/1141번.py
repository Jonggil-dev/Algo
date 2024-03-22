N=int(input())
depth={}
r=0
def check(word):
    global r
    tmp=depth
    for i in word:
        if i not in tmp:
            tmp[i]={}
        tmp=tmp[i]
    if 0 not in tmp and len(tmp)==0:
        r+=1
        tmp[0]=1
words=sorted([input() for _ in range(N)],reverse=True)
for word in words:
    check(word)
print(r)