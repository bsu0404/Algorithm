N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

cnt=0
crane.sort(reverse=True) # 큰 것부터
box.sort()
if box[-1] > crane[0]:
    print(-1)
    exit()

while box:
    cnt += 1
    tmp = []
    for x in crane:
        while box and box[-1] > x:
            tmp.append(box.pop())
        if box:
            box.pop()
    box = box + tmp[::-1]


print(cnt)