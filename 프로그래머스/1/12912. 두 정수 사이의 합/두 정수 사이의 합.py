def solution(a, b):
    s=0
    mi=min(a,b)
    ma=max(a,b)
    for i in range(mi,ma+1):
        s=s+i
    return s