N = int(input())

tmp = 2**32 - N # 보수
result = bin(tmp ^ N)
print(result.count('1'))
