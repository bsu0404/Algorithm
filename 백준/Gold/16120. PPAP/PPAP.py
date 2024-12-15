stack = []
str = input()

for s in str:
    stack.append(s)
    if len(stack) >= 4 and ''.join(stack[-4:]) == "PPAP":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("P")

print("PPAP" if stack.pop() == "P" and len(stack) == 0 else "NP")
