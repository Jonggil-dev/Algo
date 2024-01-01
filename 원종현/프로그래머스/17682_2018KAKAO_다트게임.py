def solution(dartResult):
    dartResult+='0S'
    c=0
    sq={'S':1,'D':2,'T':3}
    points=[0]
    while c<len(dartResult):
        if dartResult[c].isnumeric():
            if dartResult[c:c+2]=='10':
                points.append(int(dartResult[c]+'0')**sq[dartResult[c+2]])
                c+=1
            else:
                points.append(int(dartResult[c])**sq[dartResult[c+1]])
            c+=1
        if dartResult[c]=='*':
            points[-1]=points[-1]*2
            points[-2]=points[-2]*2
        if dartResult[c]=='#':
            points[-1]+=-2*points[-1] if 0<=points[-1] else points[-1]
        c+=1
    answer = sum(points)
    return answer