def solution(t, p):
    i=0
    result=0
    while i <=len(t)-len(p):
        tmp=t[i:i+len(p)]
        if tmp<= p:
            result=result+1
        i = i+1
    return result



