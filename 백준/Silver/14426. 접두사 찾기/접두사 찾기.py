N, M = map(int, input().split())

arr1 = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]

root = [-1, False, {}]
# value 없어도 되지 않나?
for word in arr1:
    p = root
    for c in word:
        if c not in p[2]:
            p[2][c] = [c,False, {}]
        p = p[2][c]
    p[1] = True
ans = 0
for word in arr2:
    p = root
    flag = True
    for c in word:
        if c in p[2]:
            p = p[2][c]
        else:
            flag = False
    if flag == True:    
        ans += 1
print(ans)