N = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum = 0
ans = 0

for time in arr:
    sum += time
    ans += sum

print(ans)

