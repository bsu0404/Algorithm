N = int(input())
postfixExpression = input()
value = list(int(input()) for _ in range(N))
operator= ["+","-","*","/"]
stack = []
def calculate(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return b - a
    elif op == '*':
        return a * b
    elif op == '/':
        return b / a

for s in postfixExpression:
    if s in operator:
        a = stack.pop()
        b = stack.pop()
        res  = calculate(a,b,s)
        stack.append(res)
    else:
        stack.append(value[ord(s) - ord("A")])

print("%0.2f"%res)