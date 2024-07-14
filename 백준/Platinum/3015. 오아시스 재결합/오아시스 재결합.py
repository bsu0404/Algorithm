import sys
input = sys.stdin.readline

N = int(input())
tall = []
for i in range(N) :
    tall.append(int(input()))
stack = []
cnt = 0

for t in tall :
    # stack에 데이터가 존재하고 마지막 스택의 애의 키가 이번 t보다 작으면
    while stack and t > stack[-1][0] < t :
        temp = stack.pop()[1]
        cnt += temp
    
    #스택이 비어있으면
    if not stack :
        stack.append([t, 1])

    #스택이 비어있지 않은 경우
    else :
        # 만약에 마지막애랑 키가 같으면
        if stack[-1][0] == t :
            # 만약에 스택에 여러명이 있는 경우 보이는 인원수 + 1명을 더 볼 수 있기 때문에 데이터 값 추가
            cnt += stack[-1][1]
            stack[-1][1] += 1
            if len(stack) > 1 :
                cnt += 1
        # 키가 같지 않다면 그냥 스택에 추가하고 + 1
        else :
            stack.append([t, 1])
            cnt +=1

print(cnt)

# 5
# 8
# 1
# 1
# 5
# 4