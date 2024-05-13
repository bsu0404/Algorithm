N = int(input())
N = N - 1 # 본인 외 투표자

received = int(input())
r = received
arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

while arr and arr[0] >= received:
    received += 1
    arr[0] -= 1
    arr.sort(reverse=True)
print(received - r)
