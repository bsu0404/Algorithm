import sys
input = sys.stdin.readline

N = int(input())

arr = [input() for _ in range(N)]
root =  [{}, 0]
for word in arr:
    p = root
    s = ""
    flag = False
    for w in word:
        s += w
        if w not in p[0]:
            p[0][w] = [{}, 0]
            if flag == False:
                print(s.strip())
                flag = True
             
        p = p[0][w]
    p[1] += 1

    if flag == False:
        if p[1] == 1:
            print(s.strip())
        else: 
            print(s.strip(),str(p[1]),sep="")
        
