N, M = map(int, input().split()) # 세로 가로


if N == 1 or M == 1:
    print(1)
elif N >= 3 and M >= 7:
    print(M - 2)
elif N < 3 and M >= 7:
    print(4)
elif N >= 3 and M < 7:
    print(min(M, 4))
elif N < 3 and M < 7:
    print(M // 2 + M % 2)