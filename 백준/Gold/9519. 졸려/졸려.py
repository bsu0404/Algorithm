import sys
N = int(input())
string = input()
result = string
cnt=0
while True: #한바퀴 도는 지점 cnt
    cnt+=1
    even = [char for index, char in enumerate(result) if index % 2 == 0]
    odd = [char for index, char in enumerate(result) if index % 2 != 0]
    odd.reverse()
    result = even + odd
    if cnt == N:
        print("".join(result))
        sys.exit()
    if result ==list(string):
        break
for _ in range((N-cnt)%cnt):
    even = [char for index, char in enumerate(result) if index % 2 == 0]
    odd = [char for index, char in enumerate(result) if index % 2 != 0]
    odd.reverse()
    result = even + odd

print("".join(result))
