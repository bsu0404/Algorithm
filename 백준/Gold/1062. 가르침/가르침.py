import sys
sys.setrecursionlimit(10 ** 6)

def findComb(idx):
    global maxCount
    
    if len(alphabet) == K:
        count = 0
        for i in range(N):
            if wordsSet[i] - alphabet == set():
                count += 1
        if maxCount < count:
            maxCount = count
        maxCount = max(maxCount, count)
        return
         
    if idx == 26:
        return
    
    newC = chr(ord('a') + idx)

    if newC not in alphabet and newC in usedSet:
        alphabet.add(newC)
        findComb(idx+1)
        alphabet.remove(newC)
    findComb(idx+1)
    
N, K = map(int, input().split())
words = list(input() for _ in range(N))
wordsSet = []
usedSet = set(['a','n','t','c','i'])
alphabet = set(['a','n','t','c','i'])
maxCount = 0



for word in words:
    wordsSet.append(set(word[4:-4]))
    usedSet.update(word[4:-4])

if K < 5:
    print(0)
    sys.exit()

if K >= len(usedSet):
    print(N)
    sys.exit()
    

findComb(1)

print(maxCount)

