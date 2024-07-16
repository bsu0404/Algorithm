N = int(input())

lenArr = [3]

for i in range(1,30):
    lenArr.append(2 * lenArr[i - 1] + i + 3)   

k = 0
while N > lenArr[k] : 
    k += 1

while True:
    

    if k == 0 and N == 1:
        print('m')
        break
    elif k == 0:
        print('o')
        break


    size1 = lenArr[k - 1]
    size2 = k + 3

    part1 = 1
    part2 = part1 + size1 
    part3 = part2 + size2 


    if N in (part1, part2, part3):
        print('m')
        break

    # part1 : 앞
    if part1 <= N < part2:
        k -= 1 

    # part2: 가운데
    elif part2 <= N < part3:
        print('o')
        break

    # part3: 뒤
    else:
        N = N - size1 - size2
        k -= 1