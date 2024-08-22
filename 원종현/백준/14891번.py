wheel=[input() for _ in range(4)]
K=int(input())
center=[0,0,0,0]
def get_left_right(idx):
    left=wheel[idx][center[idx]-2]
    right=wheel[idx][(center[idx]+2)%8]
    return left,right

def conv_center(center_idx):
    return (center_idx+8)%8

def func(rotate_num,dir,flag):
    global center
    nowl,nowr=get_left_right(rotate_num)
    center[rotate_num]=(center[rotate_num]-dir+8)%8
    if flag==1 or flag==2:
        if rotate_num!=3:
            rl,rr=get_left_right(rotate_num+1)
            if nowr!=rl:
                func(rotate_num+1,-dir,1)

    if flag==0 or flag==2:
        if rotate_num!=0:
            ll,lr=get_left_right(rotate_num-1)
            if nowl!=lr:
                func(rotate_num-1,-dir,0)
for i in range(K):
    a,b=map(int,input().split())
    func(a-1,b,2)
print(sum([int(wheel[i][center[i]])*(2**(i)) for i in range(4)]))