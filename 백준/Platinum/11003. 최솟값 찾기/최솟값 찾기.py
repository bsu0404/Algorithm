from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

queue = deque()
result = []

for i in range(N):
    # 현재 인덱스랑 슬라이싱 윈도우의 범위를 비교해서 범위가 벗어나면 앞쪽 원소를 제거
    if queue and queue[0] < i - L + 1:
        queue.popleft()
    
    # 덱의 뒷부분에서부터 현재 원소보다 큰 원소 제거
    while queue and A[queue[-1]] > A[i]:
        queue.pop()
    
    queue.append(i)
    
    # 현재 윈도우의 최솟값을 결과에 저장
    result.append(A[queue[0]])

print(" ".join(map(str, result)))
