N = int(input())

lenArr = [3]

for i in range(1,30):
    lenArr.append(2 * lenArr[i - 1] + i + 3)   

k = 0
while N > lenArr[k] : 
    k += 1

s = 1
while True:
    if k == 0 :
        if s == 0 :
            print('m')
        else :
            print('o')
        break

    # 각 구역의 사이즈 결정자 = k
    size1 = lenArr[k-1]
    size2 = k + 3
    part1 = s
    part2 = part1 + size1
    part3 = part2 + size2
    
    if N in (part1, part2, part3) :
        print('m')
        break

    # part1 : 첫 번째 구역
    if N < part2:
        s = part1
    # part2 : 두 번째 구역
    elif part2 <= N < part3:
        print('o')
        break
    # part3 : 세 번째 구역
    else: # part3 <= N
        s = part3

    k -= 1

