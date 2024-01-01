def solution(m, musicinfos):
    answer_list = [] # 네오가 들은 음(m)이 곡에 포함된 경우, 여기에 시간과 곡 이름을 추가
    for info in musicinfos:
        start, end, name, melody = info.split(',') # 구분자가 , 이므로 , 로 split
        hh = int(end[0:2]) - int(start[0:2])
        mm = int(end[3:]) - int(start[3:])
        if mm < 0:
            hh -= 1
            mm = 60 + mm

        play_time = hh * 60 + mm # 총 재생시간을 분으로 바꿈

        melody_list = [] # melody 문자열의 길이일 뿐, 음의 개수는 아님 -> #이 붙은 음도 있으므로
        i = 0
        while i < (len(melody) - 1): # melody 순회하면서 뒤에 오는 문자가 #이면 #까지 포함해서 melody_list에 저장, 아니면 그 문자만 저장 -> melody에 포함된 음을 구분하는 용도
            if melody[i + 1].isalpha():
                melody_list.append(melody[i])
                i += 1
            else:
                melody_list.append(melody[i]+melody[i+1])
                i += 2
        if i == len(melody) - 1:
            melody_list.append(melody[i])

        total_melody = ''.join(melody_list * (play_time // len(melody_list)) + melody_list[0:(play_time % len(melody_list))])
        # 총 플레이 시간동안 재생된 음들을 //와 %를 사용하여 리스트 형태로 구하고 문자열로 만듬
        # print(total_melody)

        while total_melody.find(m) != -1: # total_melody에 네오가 들은 음(m)이 있으면
            idx = total_melody.find(m) # 인덱스를 구해서
            if idx + len(m) == len(total_melody): # 인덱스 + m의 길이가 total_melody의 전체 길이와 같으면 -> 끝에 오는 문자가 없다는 말
                answer_list.append((play_time, name)) # 정답이 될 수 있음
                break
            else: # 인덱스 + m의 길이가 total_melody의 전체 길이와 같지 않으면 -> 뒤에 #이 있을 수 있음
                if total_melody[idx+len(m)] != '#': # #이 없으면 -> 정답이 될 수 있음
                    answer_list.append((play_time, name))
                    break
                else: # #이 있으면, m+'#'을 total_melody에서 제거하고 다시 m 있는지 확인
                    total_melody = total_melody.replace(m+'#', '')

    if answer_list:
        answer_list.sort(key=lambda x: -x[0])
        # 정답이 여러 개 있으면, 재생 시간이 제일 긴 음악이 정답이 되고, 재생 시간이 같으면 먼저 입력된 음악이 정답이 되므로 play_time 기준 내림차순 정렬
        # print(answer_list)
        return answer_list[0][1] # 곡 제목 return
    else:
        return '(None)'

# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

# m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

# m =
print(solution(m, musicinfos))

