from collections import Counter

def solution(str1, str2):
    answer = 0
    li1, li2 = [], []
    str1, str2 = str1.lower(), str2.lower()
    
    for i in range(0, len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            li1.append(str1[i: i + 2])
        
    for j in range(0, len(str2) - 1):
        if str2[j].isalpha() and str2[j + 1].isalpha():
            li2.append(str2[j: j + 2])
    
    intersection = set(li1) & set(li2)
    C1, C2 = Counter(li1), Counter(li2)
    
    iv = 0
    for e in intersection:
        iv += min(C1[e], C2[e])
    
    uv = len(li1) + len(li2) - iv
    
    if uv == 0:
        return 65536
    
    return int((iv / uv) * 65536)