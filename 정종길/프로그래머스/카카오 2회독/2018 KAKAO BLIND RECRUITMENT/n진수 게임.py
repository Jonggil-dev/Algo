def solution(n, t, m, p):
    answer = ""
    text = ""
    base = "0123456789ABCDEFG"

    for num in range(t * m):
        text += parse(num, n, base)
    
    for i in range(p - 1, t * m, m):
        answer += text[i] 
    
    return answer

def parse(num, n, base):
    
    parse_num = ""
    while num >= n:
        num, r = divmod(num, n)
        parse_num = base[r] + parse_num
    
    parse_num = base[num] + parse_num
    
    return parse_num
    