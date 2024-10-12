N=int(input())

for i in range(N-1):
    print('* '*i+"*"*(1+4*(N-i-1))+" *"*i)
    print('* '*(i+1)+" "*(1+4*(N-i-2))+' *'*(i+1))

print("* "*(2*N-1))

for i in range(N-1):
    print('* '*(N-i-1)+" "*(1+4*i)+' *'*(N-i-1))
    print('* '*(N-i-2)+"*"*(1+4*(i+1))+' *'*(N-i-2))
