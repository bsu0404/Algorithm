R, C = map(int, input().split())
mtx = [[0] * (C + 1)] + [[0] + list(map(int, input())) for _ in range(R)]
sumMtx = [[[0,0] for _ in range(C + 2)] for _ in range(R + 1)]
for i in range(1,R + 1):
    for j in range(1,C + 1):
        if mtx[i][j] == 1:
            sumMtx[i][j][0] = sumMtx[i-1][j-1][0] + 1
            sumMtx[i][j][1] = sumMtx[i-1][j+1][1] + 1

ans = 0
for i in range(1, R + 1):
    for j in range(1, C + 1):
        tmp = min(sumMtx[i][j])
        for s in range(tmp, ans , -1):
            if 0 <= i - s + 1 <= R + 1 and 0 <= j - s + 1 <= C + 1 and 0 <= j + s - 1 <= C + 1:
                l = sumMtx[i - s + 1][j - s + 1][1] >= s
                r = sumMtx[i - s + 1][j + s - 1][0] >= s
                if l and r and ans < s:
                    ans = s
                    break

print(ans)