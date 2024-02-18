from collections import deque

N,K= map(int,input().split())

def bfs():
    minCount = float("inf")
    case =0 
    needVisit = deque()
    x = N
    visited = [0] *100001 
    needVisit.append([x,0])
    visited[x] = 1
    
    while len(needVisit)>0:
        x, count = needVisit.popleft()

        MOVE = [x,-1,1] 
        if x == K :
            if count<minCount: #작으면
                case=0

            if count<=minCount: #작으면, 같으면
                case+=1 
                minCount = count

        else:
            for i in range(3):
                nx = x +  MOVE[i]           
                if (0 <= nx <= 100000)  and ((visited[nx] ==0) or (visited[nx] >= count)) :
                    visited[nx] = count
                    needVisit.append([nx,count+1])
                        
                        
    print(minCount)
    print(case)

bfs()