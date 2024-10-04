n = int(input())

words = [input() for _ in range(n)]
count = 0

for word in words:
    alphabet = set()
    
    for i in range(len(word)):
        char = word[i]
        # 나온 적 없는 알파벳 또는 앞글자랑 같은 알파벳
        if char not in alphabet or word[i - 1] == char:
            alphabet.add(char)
        else:
            break
        # 그룹단어 count
        if i == len(word) - 1:
            count += 1

print(count)
    
