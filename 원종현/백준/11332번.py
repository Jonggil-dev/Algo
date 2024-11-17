import math
for _ in range(int(input())):
    li=input().split()
    tmp=li[0]
    N,T,L=map(int,li[1:])
    limit=(10**8)*L
    if tmp=="O(N)":
        if N*T<=limit:
            print('May Pass.')
        else:
            print('TLE!')
    if tmp=='O(N^2)':
        if ((N**2)*T)<=limit:
            print('May Pass.')
        else:
            print('TLE!')
    if tmp=='O(N^3)':
        if ((N**3)*T)<=limit:
            print('May Pass.')
        else:
            print('TLE!')
    if tmp=='O(2^N)':
        if ((2**N)*T)<=limit:
            print("May Pass.")
        else:
            print('TLE!')
    if tmp=='O(N!)':
        if (math.factorial(N)*T)<=limit:
            print('May Pass.')
        else:
            print('TLE!')