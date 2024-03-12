def solution(new_id):
    from collections import deque
    ls = deque()
    for i in new_id:
        if i.isalpha() or i.isnumeric() or i in ['.', '-','_']:
            if i.isalpha():
                ls.append(i.lower())
            else:
                ls.append(i)
    for i in range(len(ls)-1):
        if ls[i] == '.' and ls[i+1] == '.':
            ls[i] = ''
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == '' or ls[i] == '.':
            cnt += 1
        else:
            break
    for i in range(cnt):
        ls.popleft()
    
    cnt = 0
    for i in range(len(ls)-1,-1,-1):
        if ls[i] == '' or ls[i] == '.':
            cnt += 1
        else:
            break
    for i in range(cnt):
        ls.pop()
        
    answer = ''.join(ls)
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    if answer == '':
        answer = 'a'
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    print(ls)
    return answer
