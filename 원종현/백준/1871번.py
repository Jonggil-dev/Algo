for i in range(int(input())):
    S=input()
    r1=sum([(ord(S[i])-65)*(26**(2-i)) for i in range(3)])
    r2=int(S[4:])
    print('nice' if abs(r1-r2)<=100 else 'not nice')