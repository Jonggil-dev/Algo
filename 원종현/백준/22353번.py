a,d,k=map(int,input().split())
def func(d):
    if d>=100:
        return a
    return d*0.01*a+(100-d)*0.01*(a+func(d*(1+k*0.01)))
print("%.10f"%(func(d)))