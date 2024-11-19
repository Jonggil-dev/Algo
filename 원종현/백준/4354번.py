def KMP_table(pattern):
    len_pattern=len(pattern)
    tmp_table=[0]*len_pattern

    p_idx=0
    for idx in range(1,len_pattern):
        while p_idx>0 and pattern[idx]!=pattern[p_idx]:
            p_idx=tmp_table[p_idx-1]

        if pattern[idx]==pattern[p_idx]:
            p_idx+=1
            tmp_table[idx]=p_idx
    return tmp_table

while True:
    S=input()
    if S=='.':
        break
    t=KMP_table(S)
    if not len(S)%(len(S)-t[-1]):
        print(len(S)//(len(S)-t[-1]))
    else:
        print(1)