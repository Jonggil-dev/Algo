def solution(n):
    answer = 0
    ls = [-1]*60001
    ls[1] = 1
    ls[2] = 2
    ls[3] = 3
    for i in range(4,n+1):
        ls[i] = (ls[i-1] + ls[i-2]) % 1000000007
    return ls[n] 
