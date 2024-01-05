from collections import deque
def solution(n, t, m, timetable):
    timetable=deque(sorted([int(i[:2])*60+int(i[3:]) for i in timetable]))
    bus=540-t
    for i in range(n-1):
        bus+=t
        for _ in range(m):
            if timetable and timetable[0]<=bus:
                timetable.popleft()
            else:
                break
    bus+=t
    time=bus if len(timetable)<m or timetable[m-1]>bus else timetable[m-1]-1
    return str(time//60).zfill(2)+":"+str(time%60).zfill(2)
n=int(input())
t=int(input())
m=int(input())
timetable=eval(input())
print(solution(n,t,m,timetable))