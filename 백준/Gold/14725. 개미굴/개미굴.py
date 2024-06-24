# function
def dfs(p, depth):

    words = sorted(p)
    for w in words:
        print("-"*(2*depth), w, sep="")
        dfs(p[w], depth+1)

# main

N = int(input())
arr = [list(input().split())[1:] for _ in range(N)]

root = {}
for words in arr:
    p = root
    for word in words :
        if word not in p :
            p[word] = {}
        p = p[word]

dfs(root, 0)