def solution(s):
    answer = []
    txt_ls = []
    set_ls = []
    res = set()
    
    i = 1
    while i < len(s) - 1:
        if s[i] == "{":
            tmp = ""
        elif s[i] == "}":
            txt_ls.append(tmp)
        else:
            tmp += s[i]
        i += 1

    for txt in txt_ls:
        set_ls.append(txt.split(","))
    
    set_ls.sort(key = lambda x : len(x))
    
    
    for s in set_ls:
        for num in s:
            if int(num) not in res:
                res.add(int(num))
                answer.append(int(num))
                
    return answer