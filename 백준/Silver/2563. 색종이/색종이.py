N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
paper = [[0] * 100 for _ in range(100)]

cnt = 0

for x, y in arr:
    i = x
    while i < x + 10:
        j = y
        while j < y + 10:
            #  이미 색종이가 올라간 경우
            if paper[i][j] != 0:
                j = paper[i][j]
            else:
                paper[i][j] = y + 10
                j += 1
                cnt += 1
        i += 1

print(cnt)
