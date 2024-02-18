import heapq
import sys
input = sys.stdin.readline

T = int(input())

def cal():
    N = int(input())
    minHeap = []
    maxHeap = []
    cnt = 0 
    nums = {}

    for _ in range(N):
        f,n = input().split()
        n = int(n)
        if f == "I": 
            cnt += 1
            if n in nums: nums[n] +=1 # 몇개인지 관리할 수 있으므로 또 넣을 필요 x
            else: 
                nums[n] = 1 
                heapq.heappush(minHeap, n)
                heapq.heappush(maxHeap, -n)

        elif f == "D" and n<0 and cnt>0: # 최소 삭제
    
            while minHeap[0] not in nums or nums[minHeap[0]] < 1:
                r = heapq.heappop(minHeap)
                if r in nums: del(nums[r])
                
            nums[minHeap[0]] -= 1
            cnt -= 1           

        elif f == "D" and n>0 and cnt>0: # 최대 삭제
            while -maxHeap[0] not in nums or nums[-maxHeap[0]] < 1:
                # 최댓값의 개수가 0개 이하인 경우 지움
                r = -heapq.heappop(maxHeap)
                if r in nums: del(nums[r])
                
            nums[-maxHeap[0]] -= 1
            cnt -= 1  
                
    if cnt>0:
        while -maxHeap[0] not in nums or nums[-maxHeap[0]] < 1:
                r = -heapq.heappop(maxHeap)
        while minHeap[0] not in nums or nums[minHeap[0]] < 1:
                r = heapq.heappop(minHeap)
        print(-maxHeap[0], minHeap[0])
    else:
        print("EMPTY")
       
for _ in range(T):
    cal()

