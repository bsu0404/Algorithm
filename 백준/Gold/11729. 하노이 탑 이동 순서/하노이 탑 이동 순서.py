N = int(input())

ans = []
count = 0
def hanoi(N, start, mid, end ) :
    global ans, count
    if N==1:
        ans.append(f"{start} {end}")
        count+=1
    else:
        hanoi(N-1,start,end,mid)
        ans.append(f"{start} {end}")
        count +=1
        hanoi(N-1,mid,start,end)

hanoi(N,1,2,3)
print(count)
print('\n'.join(ans))