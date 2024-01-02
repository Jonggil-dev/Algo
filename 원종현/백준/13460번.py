d=[0,0,1,-1] # 좌 우 하 상
N,M=map(int,input().split())
li=[]
ball={}
end=(0,0)
ball_count=2
for i in range(N):
    tmp=[k for k in input()]
    for j in range(M):
        if tmp[j]=='B':
            ball[(i,j)]=ball_count
            ball_count+=1
            tmp[j]='.'
        elif tmp[j]=='R':
            ball[(i,j)]=1
            tmp[j]='.'
        elif tmp[j]=='O':
            end=(i,j)
    li.append(tmp)
def move(r,ball):
    tmp=[]
    tmp_dic={}
    for (x,y) in ball.keys():
        bn=ball[(x,y)]
        nx,ny=x,y
        co=0
        while True:
            nx+=d[r]
            ny+=d[3-r]
            if not(0<=nx<N and 0<=ny<M) or li[nx][ny]=='#' or li[nx][ny]=='O':
                if li[nx][ny]=='O':
                    tmp.append((co,nx,ny,bn))
                else:
                    tmp.append((co,nx-d[r],ny-d[3-r],bn))
                break
            co+=1
    tmp.sort(key=lambda x:x[0])
    for co,nx,ny,bn in tmp:
        if (nx,ny) not in tmp_dic:
            if (nx,ny)==end:
                tmp_dic[(nx,ny)]=[bn]
            else:
                tmp_dic[(nx,ny)]=bn
        else:
            if (nx,ny)==end:
                tmp_dic[(nx,ny)].append(bn)
                continue
            while True:
                nx-=d[r]
                ny-=d[3-r]
                if (nx,ny) not in tmp_dic:
                    tmp_dic[(nx,ny)]=bn
                    break
    return tmp_dic



res=11
def func(cnt,ball,before,moves):
    global res
    if cnt>=res:
        return

    for i in range(4):
        if i==before:
            continue
        t_ball=move(i,ball)
        #print(ball,t_ball,cnt)
        if end in t_ball:
            if len(t_ball[end])>=2 or t_ball[end][0]!=1:
                continue
            else:
                #print(cnt,ball,t_ball,moves+[i])
                res=min(res,cnt+1)
        func(cnt+1,t_ball,i,moves+[i])
func(0,ball,-1,[])
print(res if res!=11 else -1)