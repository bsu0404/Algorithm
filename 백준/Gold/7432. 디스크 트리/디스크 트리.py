# function
def dfs(p, depth):
    # 키 기준 정렬

    words = sorted(p)
    for w in words :
        print(' ' * depth + w, sep = '')
        dfs(p[w], depth+1)

# main
N = int(input())
S = [input() for _ in range(N)]
root = {}
for s in S:
    words = s.split("\\")

    p = root
    for word in words :
        if word not in p :
            p[word] = {}
        p = p[word]

dfs(root, 0)