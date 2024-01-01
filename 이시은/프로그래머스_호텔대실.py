# 프로그래머스 호텔 대실

# 최소한의 객실만을 사용하여 예약 손님들을 받으려고 한다
# 퇴실 후 10분 간 청소 후 다음 손님 받을 수 있음
# 필요한 최소 객실의 수를 반환


def solution(book_time):
    for i, time in enumerate(book_time):
        book_time[i] = [int(time[0][0:2]) * 60 + int(time[0][3:]), int(time[1][0:2]) * 60 + int(time[1][3:]) + 10]
    book_time.sort(key=lambda x: (x[0], x[1]))
    # print(book_time)

    rooms = [book_time[0]]
    for time in book_time[1:]:
        start = time[0]
        for n_room, room in enumerate(rooms):
            if room[1] <= start:  # 방에 이미 있는 손님의 퇴실 시간 + 10분 <= 들어올 손님의 입실 시간 이면, 그 방에 손님 넣고 break
                rooms[n_room] = time
                break

        else:
            rooms.append(time)

    answer = len(rooms)
    return answer


'''
다른 사람의 풀이
from collections import Counter
def solution(book_time):
    def get_time(t):
        HH, MM = map(int, t.split(":"))
        return HH*60 + MM
    m = 0
    n = 0

    in_time = Counter([get_time(b[0]) for b in book_time])
    out_time = Counter([get_time(b[1])+10 for b in book_time])
    total_time = set(list(in_time.keys())+list(out_time.keys()))
    total_time = list(total_time)
    total_time.sort()
    for t in total_time:
        n -= out_time[t]
        n += in_time[t]
        m = max(m, n)
    return m


# 배열을 사용한 풀이
def solution(book_time):
    time_table = [0 for _ in range(60 * 24)] # 0시 00분 ~ 23시 59분의 각 분을 인덱스로 가지는 리스트 생성
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1: # 인덱스가 time_table을 넘지 않도록 방어코드 작성
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1

    return max(time_table) # 시간이 겹친다 -> 방이 겹치는 시간 횟수만큼 필요하다
    # 추가 아이디어: 위의 반복문 대신에 시작 시간은 +1, 끝 시간은 -1만 하고 마지막에 max(누적합)을 구해도 됨
'''

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
book_time = [["00:01", "00:10"], ["00:19", "00:29"]]  # 2
book_time = [["08:00", "08:30"], ["08:00", "13:00"], ["12:30", "13:30"]]  # 2
book_time = [["16:00", "16:10"], ["16:20", "16:30"], ["16:40", "16:50"]]  # 2
book_time = [["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]]  # 1
book_time = [["10:00", "10:10"]]  # 1
book_time = [["09:10", "10:10"], ["09:10", "10:10"], ["10:20", "12:20"], ["10:20", "12:20"]]  # 2
book_time = [["05:57", "06:02"], ["04:00", "06:59"], ["03:56", "07:57"], ["06:12", "08:55"], ["07:09", "07:11"]]  # 3

print(solution(book_time))

