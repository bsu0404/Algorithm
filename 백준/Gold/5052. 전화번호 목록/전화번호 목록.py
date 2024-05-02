import sys

#function

def findConsistency(n):
    l = len(numbers[n])

    if numbers[n] == numbers[n+1][:l]:
        return False
    return True


#main

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    numbers = []
    N = int(sys.stdin.readline().rstrip())

    for _ in range(N):
        numbers.append(sys.stdin.readline().rstrip())

    numbers.sort()

    result = True
    for i in range(N -1): 
        result = findConsistency(i)
        if not result:
            print("NO")
            break
    if result:
        print("YES")
    
