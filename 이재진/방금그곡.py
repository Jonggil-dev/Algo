def solution(a, musicinfos):
    m = list(a)
    ls = []
    for i in m:
        if i != "#":
            ls.append(i)
        else:
            ls[-1] = ls[-1].lower()
    m = "".join(ls)
    
    answer = "(None)"
    dic = {}
    for info in musicinfos:
        start,end,name,k = info.split(",")
        start = int(start[:2])*60 + int(start[3:])
        end = int(end[:2])*60 + int(end[3:])
        
        time = end - start
        ls = []
        for i in k:
            if i == "#":
                ls[-1] += "#"
            else:
                ls.append(i)
        for i in range(len(ls)):
            if ls[i][-1] == "#":
                ls[i] = ls[i][0].lower()
        music_len = len(ls)
        tmp = ""
        for _ in range(time // music_len):
            tmp += "".join(ls)
        for i in range(time % music_len):
            tmp += ls[i]
        
        dic[tmp] = [name,time]
    
    time = 0
    for music in dic.keys():
        if m in music:
            if time < dic[music][1]:
                time = dic[music][1]
                answer = dic[music][0]
    print(dic)
    return answer
