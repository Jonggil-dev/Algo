def solution(n, t, m, p):
    global n_num
    all_word =''
    answer = ''

    for i in range(t * m + 1):
        n_num = ''
        all_word += make_n(i, n)

    for j in range(p, t * m + 1, m):
        answer += all_word[j - 1]
        
    return answer

def make_n(num, n):
    global n_num
    
    q, t = divmod(num, n)
    word = '0123456789ABCDEF'
    
    if q == 0:
        return word[t]
    else:
        return make_n(q, n) + word[t]