T = int(input())
arr = [int(input()) for _ in range(T)]

def getCoin(price):
    coins = [25, 10, 5, 1]
    ans = []
    for coin in coins: 
        ans.append(price // coin)
        price %= coin
    return ans

for price in arr:
    result = getCoin(price)
    print(*result)
