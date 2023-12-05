def solution(arr, divisor):
    answer = []
    s=0
    for i in arr:
        if i%divisor==0:
            answer.append(i)
            s=s+1
    if s==0:
        answer.append(-1)
    answer.sort()
    return answer