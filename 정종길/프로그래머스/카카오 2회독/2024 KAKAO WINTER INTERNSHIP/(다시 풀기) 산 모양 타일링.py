def solution(n, tops):
    
    # 명품 해설 https://frontend-developer.tistory.com/entry/level-3-%EC%82%B0-%EB%AA%A8%EC%96%91-%ED%83%80%EC%9D%BC%EB%A7%81-258705
    
    an = [0] * n
    bn = [0] * n
    
    an[0] = 1
    bn[0] = 2 + tops[0]
    
    for i in range(1, n):
        an[i] = an[i - 1] + bn[i - 1]
        
        if tops[i]:
            bn[i] = (2 * an[i - 1] + 3 * bn[i - 1]) % 10007
        else:
            bn[i] = (an[i - 1] + 2 * bn[i - 1]) % 10007
            
    answer = (an[-1] + bn[-1]) % 10007
    
    return answer