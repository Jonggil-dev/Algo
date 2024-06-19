R,C=map(int,input().split())
words=[]
li=[]
for i in range(R):
    li.append(input())
li2=list(map(list,zip(*li)))
words=[]

for i in range(R):
    tmp=li[i].split('#')
    for j in tmp:
        if len(j)>1:
            words.append(j)

for i in range(C):
    tmp=''.join(li2[i]).split('#')
    for j in tmp:
        if len(j)>1:
            words.append(j)

words.sort()
print(words[0])