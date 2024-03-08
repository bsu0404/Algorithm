from math import comb

N, M, K = map(int, input().split())
length = N + M

ans = []
def getKthDict():
    global N,M,K

    if comb(N+M,N) < K:
        return -1

    for i in range(length):
        
        if N == 0:
            ans.append("z")
            continue

        value = comb(N+M-1,N-1)
        if value >= K:
            ans.append("a")
            N -= 1
        else: 
            ans.append("z")
            K -= value
            M -= 1
    return "".join(ans)

result = getKthDict()
print(result)
