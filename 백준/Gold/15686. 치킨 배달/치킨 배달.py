from itertools import combinations
import sys

INF = sys.maxsize
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

homes = []
chicken= []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            homes.append((i, j))
        elif map[i][j] == 2:
            chicken.append((i, j))

# 가능한 치킨집 조합       
comb = list(combinations(chicken, M))
ans = INF

for c in comb:
    # 해당 조합에서 최소값
    sumOfDistance = 0
    for h in homes:
        # 해당 집에서 치킨집까지 최소 거리
        minDistance = INF
        for restaurant in c:
            minDistance = min(minDistance,abs(restaurant[0]-h[0]) + abs(restaurant[1]-h[1])) 
        sumOfDistance += minDistance
    ans = min(ans, sumOfDistance)

print(ans)
