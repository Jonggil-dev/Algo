cnt=1
while True:
    A=input()
    B=input()
    if A=="END":
        break
    a=''.join(sorted(list(A)))
    b=''.join(sorted(list(B)))
    f="different" if a!=b else "same"
    print(f"Case {cnt}: {f}")
    cnt+=1