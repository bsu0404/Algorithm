N, M = map(int, input().split())

arr1 = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]

root = {}
for word in arr1:
    p = root
    for c in word:
        if c not in p:
            p[c] = {}
        p = p[c]
    p[1] = True

ans = 0
for word in arr2:
    p = root
    flag = True
    for c in word:
        if c in p:
            p = p[c]
        else:
            flag = False
    if flag == True:    
        ans += 1
print(ans)