num = list(map(int,input()))
dp =[0]*(len(num) +2)
cnt = 0
i = len(num) -1
dp[len(num)] = 1
dp[len(num)+1] = 0

while i >=  0:
    if num[i] == 0:
        i -= 1
        continue
    dp[i] += dp[i+1]
    if i + 1 < len(num):
        if  num[i]*10 + num[i+1] <= 34 :
            dp[i] += dp[i+2]
    # print(dp)
    
    i -= 1
print(dp[0])


