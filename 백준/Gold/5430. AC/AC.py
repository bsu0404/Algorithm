N = int(input())
entireArr = [[input(), int(input()), eval(input())] for _ in range(N)]

for arr in entireArr:
    cnt = 0

    for i in range(len(arr[0])):
        if arr[0][i] == 'R':
            cnt += 1
        elif arr[0][i] == 'D' and arr[1] > 0:
            if cnt % 2 == 0:
                arr[2].pop(0)
            else:
                arr[2].pop()                
            arr[1]-=1
        elif arr[0][i] == 'D' and arr[1] == 0:
            arr[1]-=1
            arr[2] ="error"
    if cnt % 2 != 0 and arr[1] > 0:
        arr[2].reverse()
        
    if arr[1] > 0:
        print("[" + ",".join(map(str, arr[2])) + "]")
    else :
        print(arr[2])