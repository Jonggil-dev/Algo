N,K=map(int,input().split(' '))
li=list(map(int,input().split(' ')))
code=[]
res=0

for this in range(K):
    if li[this]in code :  # 코드에 이미 꽂혀져있음
        continue

    if len(code)<N :  # 코드 자리 남음
        code.append(li[this])
        continue

    priority = []
    for c in code:  # 꽂혀져 있는 코드들
        if c in li[this:]: # 다음에 또 이용해야한다면
            priority.append(li[this:].index(c))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(li[this])
    res += 1
print(res)