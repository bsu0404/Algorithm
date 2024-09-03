n = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

minPrice = price[0]
ans = 0

for i in range(0, n-1):
    minPrice = min(minPrice, price[i])
    ans += (minPrice * distance[i])
print(ans)