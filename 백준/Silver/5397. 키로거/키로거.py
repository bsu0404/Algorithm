from collections import deque

def getPassword(str):
    stack1 = deque() # 답
    stack2 = deque() # 임시 스택
    
    for s in str:
        if s == "<" and stack1:
            tmp = stack1.pop()
            stack2.append(tmp)
        if s == ">" and stack2:
            tmp = stack2.pop()
            stack1.append(tmp)
        if s == "-" and stack1:
            stack1.pop()
        if "A" <= s <= "Z" or "a" <= s <= "z" or "0" <= s <= "9":
            stack1.append(s)

    while stack2:
        tmp = stack2.pop()
        stack1.append(tmp)
        
    print(*stack1,sep="")

N = int(input())

for _ in range(N):
    str = input()
    getPassword(str)

