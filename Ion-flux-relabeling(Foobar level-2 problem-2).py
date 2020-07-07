def calc(h, target, u):
    u=(u>>1)
    r_child=h-1
    l_child=h-1-u
    u-=1
    if r_child==target or l_child==target:
        return h
    else:
        if target<=l_child:
            return calc(l_child, target, u)
        else:
            return calc(r_child, target, u)
def solution(h, q):
    h=(1<<h)-1
    final=[]
    for i in q:
        if h>i>=1:
            final.append(calc(h, i, h-1))
        else:
            final.append(-1)
    return final
        
#print(solution(3,[7,3,5,1]))