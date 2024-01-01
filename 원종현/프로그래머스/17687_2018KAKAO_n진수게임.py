def solution(n, t, m, p):
    def trans(a,b):
        g='0123456789ABCDEF'
        tmp=''
        while a>0:
            a,mod=divmod(a,b)
            tmp+=str(g[mod])
        return tmp[::-1]
    answer = ''
    words='00'
    for i in range(1,t*m+1):
        words+=trans(i,n)
    answer=''.join([words[p+i*m]for i in range(t)])
    return answer