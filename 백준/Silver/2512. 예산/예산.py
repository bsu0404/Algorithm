N = int(input())
arr = list(map(int,input().split()))
M = int(input())
l = 1
r = max(arr)
while l <= r:
    mid = (l + r) // 2
    money = 0
    for cost in arr:
        if cost >= mid:
            money += mid
        elif cost < mid:
            money += cost
    if money == M:
        r = mid
        break
    elif money > M:
        r = mid - 1
    elif money < M:
        l = mid + 1

print(r)

