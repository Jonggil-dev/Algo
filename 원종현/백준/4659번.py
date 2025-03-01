import sys
input=sys.stdin.readline
t='aeiou'
while True:
    S=input().rstrip()
    check=1
    if S=='end':
        break
    for i in t:
        if i in S:
            break
    else:
        check=0
    for i in range(len(S)-2):
        a,b,c=S[i:i+3]
        if a in t and b in t and c in t:
            check=0
        if a not in t and b not in t and c not in t:
            check=0
    for i in range(len(S)-1):
        a,b=S[i:i+2]
        if a==b and a!='e' and a!='o':
            check=0
            break
    if check:
        print(f'<{S}> is acceptable.')
    else:
        print(f'<{S}> is not acceptable.')