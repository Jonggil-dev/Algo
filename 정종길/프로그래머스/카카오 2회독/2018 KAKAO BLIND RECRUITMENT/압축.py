def solution(msg):
    answer = []
    lzw = {}
    
    for n in range(65, 91):
        lzw[chr(n)] = n - 64
    
    i, word, last_num = 0, "", 27

    while i < len(msg):
        word += msg[i]
        
        if word in lzw:
            i += 1
            continue
        
        answer.append(lzw[word[:-1]])
        lzw[word] = last_num
        last_num += 1
        word = ""
        
    if word:
        answer.append(lzw[word])
        
    return answer