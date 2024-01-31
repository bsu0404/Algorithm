import sys

N,M,B=map(int,input().split())

mtx = [list(map(int,input().split())) for _ in range(N)]

minHeight = min(map(min,mtx))
maxHeight = max(map(max,mtx))
maxHeight = min(maxHeight,256)
minTime = sys.maxsize
ans = 0
height = [0] * 257

for x in mtx :
    for xx in x :
        height[xx] += 1

def leveling(goal) : # 높이를 goal로
    global minTime, height, ans
    remain = B
    time = 0
    for i in range(257): #높이가 i인 땅 계산
        count = height[i] * abs(goal-i) #채우거나 뺄 개수

        if (goal>i): #채우기
                remain -=  count
                time += count

        elif(goal<i): #빼기
            remain += count
            time += (2 * count)
        
    if (time<=minTime and remain >=0): 
        minTime = time
        ans = goal
    

for goal in range(minHeight,maxHeight+1):
    leveling(goal)

print(minTime, ans)