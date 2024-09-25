from collections import defaultdict
import math

def solution(str1, str2):
    answer = 0
    common = 0
    
    li1, li2 = make_set(str1), make_set(str2)
    a = b = 0
    
    for _, v in li1.items():
        a += v
        
    for _, v in li2.items():
        b += v

    if a > b:
        for key in li2:
            while li2[key]:
                if key in li1:
                    if not li1[key]:
                        break
                    else:
                        common += 1
                        li1[key] -= 1
                        li2[key] -= 1
                else:
                    break
    else:
        for key in li1:
            while li1[key]:
                if key in li2:
                    if not li2[key]:
                        break
                    else:
                        common += 1
                        li2[key] -= 1
                        li1[key] -= 1
                else:
                    break        
                    
    if a == 0 and b == 0:
        return 65536
    else:
        answer = common / (a + b - common)
    return math.floor(answer * 65536)


def make_set(txt):
    li = defaultdict(int)
    
    for i in range(len(txt) - 1):
        if txt[i].isalpha() and txt[i + 1].isalpha():
            li[txt[i : i + 2].lower()] += 1
    return li