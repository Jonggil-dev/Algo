A=list(map(int,input().split()))
B=list(map(int,input().split()))

if A[2]<B[0] or A[0]>B[2] or A[1]>B[3] or A[3]<B[1]:
    print('NULL')
elif (A[2]==B[0] and A[3]==B[1])or(A[0]==B[2] and A[1]==B[3])or (A[2]==B[0] and A[1]==B[3])or(A[0]==B[2] and A[3]==B[1]):
    print('POINT')
elif A[2]==B[0] or A[0]==B[2] or A[1]==B[3] or A[3]==B[1]:
    print('LINE')
else:
    print('FACE')