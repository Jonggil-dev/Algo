def solution(lines):
    answer = 0
    times=[]
    for i in lines:
        data=i.split()
        tmp=data[1].split(':')
        time=(int(tmp[0])*60+int(tmp[1]))*60000+int(float(tmp[2])*1000)
        times.append([time-int(float(data[2][:-1])*1000)+1,time])
    times.sort(key=lambda x:x[1])
    for i in range(len(times)):
        now=times[i][1]
        co=1
        for j in range(i+1,len(times)):
            if i==j:continue
            if times[j][0]-now<1000:
                co+=1
        answer=max(answer,co)
    return answer