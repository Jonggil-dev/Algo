N=int(input())
li=[input() for _ in range(N)]
if sorted(li)==li:
    print("INCREASING")
elif sorted(li,reverse=True)==li:
    print("DECREASING")
else:
    print("NEITHER")