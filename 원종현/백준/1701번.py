T=input()

def KMP_table(pattern):
    lp = len(pattern)
    tb = [0 for _ in range(lp)] # 정보 저장용 테이블

    pidx = 0 # 테이블의 값을 불러오고, 패턴의 인덱스에 접근
    for idx in range(1, lp): # 테이블에 값 저장하기 위해 활용하는 인덱스
        # pidx가 0이 되거나, idx와 pidx의 pattern 접근 값이 같아질때까지 진행
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = tb[pidx-1]

        # 값이 일치하는 경우, pidx 1 증가시키고 그 값을 tb에 저장
        if pattern[idx] == pattern[pidx] :
            pidx += 1
            tb[idx] = pidx

    return tb


table=KMP_table(T)
r=0
for i in range(len(T)):
    r=max(r,max(KMP_table(T[i:])))
print(r)