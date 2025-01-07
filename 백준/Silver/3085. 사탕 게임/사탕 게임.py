N = int(input())
arr = [input() for _ in range(N)]
sequence = [[{'r': 0, 'd': 0} for _ in range(N)] for _ in range(N)]

ans = 0

def getSequence(i,j,direction):
    x, y = 0, 0
    cnt = 0
    c = arr[i][j]
    global ans

    while i + x < N and j + y < N and arr[i+x][j+y] == c:
        cnt += 1
        sequence[i+x][j+y][direction] = max(sequence[i+x][j+y][direction],cnt)

        if direction == "r":
            y += 1
        elif direction == "d":
            x += 1

    endX = i + x
    endY = j + y        

    if direction == "r":
        endY -= 1
    if direction == "d": 
        endX -= 1
    

    if cnt == N : 
        ans = cnt
        print(cnt)
        exit()

    if direction == "r":
        
        if 0 <= j - 2 and arr[i][j-2] == c  and (i - 1 >= 0 and arr[i-1][j-1] == c or i + 1 < N and arr[i+1][j-1] == c):
            ans = max(ans, sequence[i][j-2]["r"] + cnt + 1)

        if ((j - 1 >= 0 and (i - 1 >= 0 and arr[i-1][j-1] == c or i + 1 < N and arr[i + 1][j-1] == c )) or (endY + 1 < N and (i - 1 >= 0 and arr[i-1][endY+1] == c or i + 1 < N and arr[i + 1][endY+1] == c ))):
            ans  = max(ans, cnt + 1)
        if (j - 2 >= 0 and arr[i][j-2] == c):
            ans = max(ans, cnt + 1)      
        if ans < cnt:
            ans = max(ans, cnt)
      


    elif direction == "d":
        if 0 <= i - 2 and arr[i-2][j] == c and (j - 1 >= 0 and arr[i-1][j-1] == c or j + 1 < N and arr[i-1][j+1] == c):
            ans = max(ans,sequence[i-2][j]["d"] + cnt + 1)
        if ((i - 1 >= 0 and (j - 1 >= 0 and arr[i-1][j-1] == c or j + 1 < N and arr[i - 1][j + 1] == c )) or (endX + 1 < N and (j - 1 >= 0 and arr[endX+1][j-1] == c or j + 1 < N and arr[endX + 1][j+1] == c ))):
            ans  = max(ans, cnt + 1)      
        if (i - 2 >= 0 and arr[i-2][j] == c):
            ans = max(ans, cnt + 1)
        if ans < cnt:
             ans  = max(ans, cnt)      

 


for i in range(N):
    for j in range(N):

        if sequence[i][j]["r"] == 0:   
            getSequence(i,j,"r")
        if sequence[i][j]["d"] == 0:
            getSequence(i,j,"d")

print(ans)