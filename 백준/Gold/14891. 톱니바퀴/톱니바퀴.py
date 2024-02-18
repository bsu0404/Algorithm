import copy
gears = [list(map(int,input())) for _ in range(4)]
N = int(input())
spin = [list(map(int,input().split())) for _ in range(N)]
#2, 6번이 왼쪽 오른쪽 톱니 , N = 0, S = 1
spinnedGears = copy.deepcopy(gears)

def spinning(n,direction) :
    global spinnedGears
    if direction == -1:# 반시계
        tmp = spinnedGears[n].pop(0)
        spinnedGears[n].append(tmp)
    elif direction == 1: #시계
        tmp = spinnedGears[n].pop()
        spinnedGears[n].insert(0,tmp)



for n, direction in spin: # 톱니, 방향
    n -= 1
    p, q = n + 1, n - 1
    d1,d2 = direction * (-1),direction * (-1)
    spinning(n,direction)
    while p < 4: # 오른 쪽 방향
        if gears[p][6] == gears[p-1][2]: #같은 극
            break
        else: 
            spinning(p,d1)
            d1 *=(-1)
        p += 1
        
    while q >= 0: #왼쪽 방향
        if gears[q][2] == gears[q+1][6]: #같은 극
            break
        else: 
            spinning(q,d2)
            d2 *=(-1)
        q -= 1
    gears = copy.deepcopy(spinnedGears)


ans = 0
for i in range(4):
    ans += (spinnedGears[i][0] * (2**i))
print(ans)   