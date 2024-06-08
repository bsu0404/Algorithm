N = int(input())
arr= []

for i in range(N):
    sour, bitter = input().split()
    arr.append([int(sour), int(bitter)])
ans = abs(arr[0][0] - arr[0][1])

for i in range(1,2 ** N):
    binary = bin(i)[2:].zfill(N)
    sour = 0
    bitter = 0
    for j in range(N):
        food = arr[j]
        if binary[j] =='1':
            if sour != 0:
                sour *= food[0]
            else:
                sour = food[0]
            
            bitter += food[1]
        
    if abs(sour - bitter) < ans:
        ans = abs(sour - bitter)

print(ans)