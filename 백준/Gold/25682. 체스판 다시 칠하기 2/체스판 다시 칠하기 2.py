import sys


N, M, K = map(int, input().split())

mtx = [[[0, 0] for _ in range(M + 1)]] + [[[0,0]] + list(input()) for _ in range(N)]

# [0] : 짝짝 홀홀
# [1] : 그 외

for i in range(1, N + 1):
    for j in range(1, M + 1):
        state = mtx[i][j] == "B"

        tmp = []
        tmp.append(mtx[i - 1][j][0] + mtx[i][j-1][0] - mtx[i-1][j-1][0])
        tmp.append(mtx[i - 1][j][1] + mtx[i][j-1][1] - mtx[i-1][j-1][1])
        
        if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0): # 그 외
            tmp[0] += state
        else:
            tmp[1] += state

        mtx[i][j] = tmp
ans = sys.maxsize
for i in range(K, N + 1):
    for j in range(K , M + 1):
    
        b1 = (mtx[i][j][0] - mtx[i - K][j][0] - mtx[i][j-K][0] + mtx[i-K][j-K][0])
        w1 = (K ** 2) // 2  - b1
        b2 = (mtx[i][j][1] - mtx[i - K][j][1] - mtx[i][j-K][1] + mtx[i-K][j-K][1])
        w2 = (K ** 2) // 2  - b2

        if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0): # 그 외
            w1 += K % 2 
        else: # 그 외
            w2 += K % 2

        result = min(b1+w2, b2+w1)
        ans = min(ans, result)
print(ans)