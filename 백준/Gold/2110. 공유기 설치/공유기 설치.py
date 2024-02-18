import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, C = map(int,input().split())
arr =[int(input()) for _ in range(N)]
arr.sort()
maxDistance = 0

def binarySearch(start,end):
    global maxDistance
    mid = (start+end)//2
    cnt = checkRouter(mid)

    if start > end:
        return maxDistance
    
    elif cnt >= C: #거리를 더 크게
        maxDistance = max(maxDistance,mid)
        return binarySearch(mid+1,end)

    elif cnt < C: #거리를 더 작게
        return binarySearch(start,mid-1)


def checkRouter(n): # 가능한 공유기 수

    cnt = 1
    i = 0
    j = 1
    while i + j < N:
        if arr[i] + n > arr[i+j]: #불가능한 거리
            j += 1
        elif arr[i] + n <= arr[i+j]: #가능한 거리
            cnt += 1
            i = i + j
            j = 1
    return cnt

print(binarySearch(1,arr[N-1]-arr[0]))
