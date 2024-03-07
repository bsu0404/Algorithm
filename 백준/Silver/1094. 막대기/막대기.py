N = int(input())
sum = 0;cnt = 0

for i in range(7,-1,-1):
    if sum + 2**i <= N:
        sum += 2**i
        cnt += 1

print(cnt)
    