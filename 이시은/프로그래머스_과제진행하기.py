# 프로그래머스 lv2 과제 진행하기

# 과제 계획이 나열되어 있다
# 과목명, 시작시각, 걸리는 시간
# 1. 시작시각 순으로 과제를 정렬한다
# 2. 과제를 하다가 다음 과제 시작시각이 되면 하던 과제를 남겨두고 다음 과제를 진행한다
# 하던 과제는 [과목명, 남은 시간] 순으로 stack 구조에 저장
# 3. 과제가 끝나면, 남은 과제 중 가장 최근에 하던 과제를 마저 한다
# 다음 과제 시작 시각까지 남는 시간이 있으면, stack에 있는 과제를 수행한다
# 과제가 끝나는 순서를 리턴

# 시작시각 + 걸리는 시간 => 마치는 시각 계산하는 함수
def calc_time(time, duration):
    HH = int(time[0:2])
    MM = int(time[3:])
    MM = MM + int(duration)
    while MM >= 60:
        HH += 1
        MM = MM - 60

    # HH, MM 모두 0 처리가 중요함. 숫자는 1 -> HH, MM으로는 01
    HH = "0" + str(HH) if HH < 10 else str(HH)
    MM = "0" + str(MM) if MM < 10 else str(MM)
    return ':'.join([HH, MM])


# 두 시각 사이의 간격(분)을 계산하는 함수
def calc_duration(time1, time2):
    HH = int(time1[0:2]) - int(time2[0:2])
    MM = int(time1[3:]) - int(time2[3:])
    return HH * 60 + MM


def solution(plans):
    answer = []
    stack = []
    # 과제 시작 시간 순으로 정렬
    plans = sorted(plans, key=lambda x: x[1])
    # 과제를 진행하다 다음 과제의 시작 시간이 되는지 체크
    for n in range(len(plans)-1):
        # print("stack:", stack)
        before = plans[n]
        after = plans[n+1]
        finish_time = calc_time(before[1], before[2])
        # print(before[0], finish_time, after[1])
        # 다음 과제 시작 시각보다 앞의 과제 끝나는 시간이 빠르면, 앞의 과제를 끝마칠 수 있다는 뜻 + 여유 시간이 있어서 stack에 넣은 못 다한 과제를 할 수 있음
        if finish_time < after[1]:
            answer.append(before[0])
            free_time = calc_duration(after[1], finish_time) # 여유 시간 계산
            while stack:
                # print(free_time)
                if free_time >= stack[-1][1]:
                    free_time -= stack[-1][1]
                    answer.append(stack[-1][0])
                    stack.pop()
                else:
                    # 끝내지 못하더라도 과제 수행에 남은 시간이 줄어듬
                    stack[-1][1] = stack[-1][1] - free_time
                    break

        elif finish_time == after[1]:
            answer.append(before[0])

        # 시간이 부족해서 과제를 끝내지 못한 경우 -> stack에 과목명, 남은 시간 기록
        else:
            stack.append([before[0], calc_duration(finish_time, after[1])])
    # plans의 마지막 과제를 끝낸 후, stack에 남은 과제들 수행
    answer.append(plans[-1][0])
    # print("stack:", stack)
    while stack:
        subject = stack.pop()
        answer.append(subject[0])

    return answer

plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
# plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
# plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
plans = [["1", "00:00", "30"], ["2", "00:10", "10"], ["3", "00:30", "10"], ["4", "00:50", "10"]] # 반례 -> 이걸로 코드 오류 다 고침
print(solution(plans))
