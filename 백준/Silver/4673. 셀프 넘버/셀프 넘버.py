nums = [True] * 10001

for i in range(1,10000):
    sumOfNum = i
    for j in str(i):
        sumOfNum += int(j)
        
    if sumOfNum <= 10000:
        nums[sumOfNum] = False

for i in range(1,10000):
    if nums[i] == True:
        print(i)
    