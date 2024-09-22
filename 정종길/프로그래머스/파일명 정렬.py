def solution(files):
    answer = []
    classfy = []

    for file in files:
        tail = ''
        
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):
                    if j >= 5:
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                    elif not number[j].isdigit():
                        tail = number[j:]            
                        number = number[:j]
                        break

                classfy.append((head, number, tail))
                break
                
    classfy.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for words in classfy:
        answer.append(''.join(words))
        
    return answer