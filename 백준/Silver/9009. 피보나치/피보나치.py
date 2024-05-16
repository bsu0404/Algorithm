MAXNUM = 50
fibo = [0] * MAXNUM
fibo[0] = 0
fibo[1] = 1
for i in range(2,MAXNUM):
    fibo[i] = fibo[i-1] + fibo[i-2]

T = int(input())
for _ in range(T):
    num = int(input())
    arr = []
    for j in range(MAXNUM-1, 0, -1):
        if fibo[j] <= num:
            num -= fibo[j]
            arr.append(fibo[j])
    arr = arr[::-1]
    print(*arr)

