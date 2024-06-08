import copy

s = input()
N = int(input())
minValue = 1600001

alphabet = [0] * 26
for i in range(len(s)):
    alphabet[ord(s[i]) -  ord('A')] += 1

arr = []
for _ in range(N):
    price, name = input().split()
    arr.append([int(price), name])

for i in range(1 << N):
    binary = bin(i)[2:].zfill(N)
    alphabet2 = copy.copy(alphabet)
    priceSum = 0
    
    for j in range(N): # j번째 책
        if binary[j] == '1' :
            book = arr[j][1]
            for k in range(len(book)): # j번째 책의 k번째 글자
                alphabet2[ord(book[k]) - ord('A')] -= 1
            priceSum += arr[j][0]
            
    flag = 1
    for j in range(26):
        if alphabet2[j] > 0 :
            flag = 0
    if flag == 1 and minValue > priceSum:
        minValue = priceSum
    
if minValue == 1600001:
    print(-1)
else:
    print(minValue)

