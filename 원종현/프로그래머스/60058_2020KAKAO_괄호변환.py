def check(l):
    stk=[]
    for i in range(len(l)):
        if not stk:
            stk.append(l[i])
        else:
            if stk[-1]=='(' and l[i]==")":
                stk.pop()
            else:
                stk.append(l[i])
    return 0 if stk else 1
def flip(l):
    return ''.join([")"if i=="(" else"(" for i in l])

def step2(l):
    pass
def step1(l):
    u,v='',''
    for idx in range(1,len(l)):
        u_l=l[:idx].count('(')
        v_l=l[idx:].count('(')
        if u_l==len(l[:idx])-u_l and v_l==len(l[idx:])-v_l:
            return l[:idx],l[idx:]
    return l,''

def go(p):
    if not p:
        return ''
    u,v=step1(p)
    if check(u):
        return u+go(v)
    else:
        return '('+go(v)+')'+flip(u[1:-1])

def solution(p):
    answer=go(p)
    return answer