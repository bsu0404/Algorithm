import sys
input = sys.stdin.readline

MOVE = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
SCORES = [0, 0, 0, 1, 1, 2, 3, 5, 11]

def dfs(boardIdx, i, j, p, s):
    global maxStr, score, cnt, find
    depth = len(s)

    if '$' in p :
        word = ''.join(s)
        if word not in find:
            score += SCORES[depth]
            find.add(word)

        if len(maxStr) < depth:
            maxStr = word
        elif len(maxStr) == depth:
            maxStr = min(maxStr, word)

    for x, y in MOVE:
        xx, yy = i + x, j + y

        if not (0 <= xx < 4) or not (0 <= yy < 4):
            continue

        c = boards[boardIdx][xx][yy]
        if c in p and not visited[xx][yy]:
            visited[xx][yy] = True
            dfs(boardIdx, xx, yy, p[c], s + [c])
            visited[xx][yy] = False

w = int(input().strip())
words = [input().strip() for _ in range(w)]
input().strip()

b = int(input().strip())
boards = []

for i in range(b):
    tmp = [list(input().strip()) for _ in range(4)]
    boards.append(tmp)
    if i < b - 1:
        input().strip()

root = {}
for word in words:
    p = root
    for c in word:
        if c not in p:
            p[c] = {}
        p = p[c]
    p['$'] = word 

for boardIdx in range(b):
    board = boards[boardIdx]
    find = set()
    maxStr = ""
    score = 0
    cnt = 0

    for i in range(4):
        for j in range(4):
            c = board[i][j]
            if c in root:
                visited = [[False] * 4 for _ in range(4)]
                visited[i][j] = True
                dfs(boardIdx, i, j, root[c], [c])

    print(score, maxStr, len(find))
