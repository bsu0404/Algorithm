from collections import deque

N = int(input()) #보드 크기
K = int(input()) # 사과 위치
apple = {tuple(map(int,input().split())) for _ in range(K)}
L = int(input()) # 방향 변환
direction = [list(input().split()) for _ in range(L)]

current = [0,1]

snake = deque() #left: 꼬리 
snake.append((0,0))
snakes = set()
snakes.add((0,0))
i = 0 #time
x=0
y=0
j = 0 #방향
while True:
    if j<len(direction) and int(direction[j][0]) == i:
        if direction[j][1] == "D": #우로
            new = [current[1],current[0]*(-1)]
        if direction[j][1] == "L": #좌로
            new = [current[1]*(-1),current[0]]
        current = new
        j += 1
    x = x+current[0]
    y = y+current[1]

    if (x,y) in snakes or not (0<=x<N and 0<=y<N): #머리
        print(i+1)
        break

    snake.append((x,y))
    snakes.add((x,y))

    if (x+1,y+1) not in apple: # 꼬리 자르기
        a,b = snake.popleft()
        snakes.remove((a,b))
        
    if  (x+1,y+1) in apple:
        apple.remove((x+1,y+1))
        
    i += 1


    