def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = to_sec(video_len), to_sec(pos), to_sec(op_start),to_sec(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
        
    for c in commands:
        pos = ops_check(pos, video_len, op_start, op_end)
        if c[0] == "n":
            pos += 10
        else:
            pos -= 10
    pos = ops_check(pos, video_len, op_start, op_end)
    
    return f'{pos // 60:02d}:{pos % 60:02d}'

def to_sec(mmss):
    mm, ss = int(mmss[:2]), int(mmss[3:])
    return mm * 60 + ss

def ops_check(pos, video_len, op_start, op_end):
    if pos <= 0:
        pos = 0
    elif video_len <= pos:
        pos = video_len
    
    if op_start <= pos <= op_end:
        pos = op_end
        
    return pos