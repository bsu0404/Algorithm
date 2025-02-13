
import sys 
input = sys.stdin.readline 
from collections import deque


N, M = map(int, input().split())
subordinate = [[]for _ in range(N)]
dp = [0] * N
boss = list(map(int, input().split()))

# subordinate 배열에 부하 직원 저장
for i in range(N):
    if boss[i]== -1:
        top = i
    else:
        subordinate[boss[i]-1].append(i)

# 칭찬 점수 저장
for _ in range(M):
    empNum, score = map(int, input().split())
    dp[empNum - 1] += score

stack = deque()
stack.append(top)

# 최고 직원부터 부하직원 점수 +
while stack:
    a = stack.pop()
    for emp in subordinate[a]:
        dp[emp] += dp[a]
        stack.append(emp) 

print(*dp)
