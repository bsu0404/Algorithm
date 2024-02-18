N = int(input())
arr = list(map(int,input().split()))
increasingArr = [arr[0]]

def binarySearch(start,end,goal):
    mid = (start+end)//2
    if increasingArr[mid] == goal:
        return mid
    if start > end:
        return start
    if increasingArr[mid]>goal:
        return binarySearch(start,mid -1, goal)
    elif increasingArr[mid]<goal:
        return binarySearch(mid +1 ,end,goal)

for x in arr:
    if increasingArr[-1] < x:
        increasingArr.append(x)
    else:
        idx = binarySearch(0,len(increasingArr)-1,x)
        increasingArr[idx] = x
    
print(len(increasingArr))