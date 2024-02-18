import sys
N = int(input())
K = int(input())
ans = sys.maxsize
def binarySearch(start , end):
    global K, ans
    cnt = 0
    mid = (start+end)//2

    if start > end:
        return ans
    
    for i in range(1,N+1):
        cnt += min(mid//i,N)
    if cnt >= K: #K번째 수 초과
        ans = mid
        return binarySearch(start,mid-1)
    else: #K번째 수 이하
        return binarySearch(mid+1,end)
    
print(binarySearch(1,K))
