import sys
input = sys.stdin.readline

INF = sys.maxsize
str= input().strip()
lenStr = len(str)
dp = [[False] * (lenStr + 1) for _ in range(lenStr+1)]
ans = [INF] * (lenStr+1)

for i in range(lenStr+1):
    dp[i][i] = True

for i in range(1,lenStr+1):
    for j in range(1,i):
        # 사이가 팰린드롬, 일치
        if dp[i-1][j+1] and str[i-1] == str[j-1]:
            dp[i][j] = True
        # 길이 2, 일치
        if j + 1 == i and str[i-1] == str[j-1]:
            dp[i][j] = True

ans[0] = 0
# i까지 최소 팰린드롬 분할 수 ans에 저장
for i in range(1,lenStr+1):
    ans[i] = ans[i-1] + 1

    # 본인이 팰린드롬 마지막인게 있다면 (j부터 i까지)
    for j in range(i):
        if dp[i][j]:
            ans[i] = min(ans[i], ans[j - 1] + 1)

print(ans[lenStr])