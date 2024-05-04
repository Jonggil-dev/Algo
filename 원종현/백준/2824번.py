def gcd(a,b) :
    while b > 0 :
        tmp = a%b
        a = b
        b = tmp
    return a

def multiply(lst) :
    return eval('*'.join([str(n) for n in lst]))

N = int(input())
N_l = list(map(int,input().split()))

M = int(input())
M_l = list(map(int,input().split()))

a = multiply(N_l)
b = multiply(M_l)

print('%s'%str(gcd(a,b))[-9:])