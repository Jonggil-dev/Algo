s=['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
S=input().split()
t=S[0][0].upper()
print(S)
for i in S[1:]:
    for j in s:
        if i==j:
            break
    else:
        t+=i[0].upper()
print(t)