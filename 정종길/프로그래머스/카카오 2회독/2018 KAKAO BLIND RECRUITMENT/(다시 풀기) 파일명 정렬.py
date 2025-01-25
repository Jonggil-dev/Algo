import re

def solution(files):
    answer = []
    
    for file in files:
        answer.append(re.findall(r'([a-zA-Z-\s]+)(\d{1,5})(.*)', file)[0])
    
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    answer = [''.join(file) for file in answer]
    
    return answer