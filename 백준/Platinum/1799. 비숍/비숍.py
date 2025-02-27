import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# functuion
def findComb(idx, possible, i):
     
    if idx == len(possible):
        ans[i] = max(ans[i], len(combSum))
        return

    x, y = possible[idx]
    # 비숍 놓기 가능한 경우
    if x + y not in  combSum and x-y not in combSub:
        combSum.add(x + y)
        combSub.add(x - y)
        findComb(idx+1, possible, i)
        combSum.remove(x + y)
        combSub.remove(x - y)
    # 비숍을 놓지 않는 경우
    
    findComb(idx+1, possible, i)

# main
N = int(input())
mtx = [list(map(int,input().split())) for _ in range(N)]
possible_white = []
possible_black = []

combSum = set()
combSub = set()

ans = [0,0]

for i in range(N):
    for j in range(N):
        if mtx[i][j] == 1 and (i + j) % 2 == 0:
            possible_black.append((i,j))
        elif mtx[i][j] == 1 and (i + j) % 2 == 1:
            possible_white.append((i,j))


findComb(0,possible_black,0)
findComb(0,possible_white,1)


print(sum(ans))