N=int(input())
li=list(map(int,input().split()))
if N==1:
    print("권병장님, 중대장님이 찾으십니다")
else:
    li2=list(map(int,input().split()))
    st=[li[0]+li2[0]]
    for i in range(N-1):
        if li[i]<=st[-1]:
            if li[i]+li2[i]>=st[-1]:
                st.pop()
                st.append(li[i]+li2[i])
        else:
            break
    if li[N-1]<=st[-1]:
        print("권병장님, 중대장님이 찾으십니다")
    else:
        print("엄마 나 전역 늦어질 것 같아")