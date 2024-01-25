import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

num = int(input())
N = 4*num-3

array = [[' ' for _ in range(N)] for _ in range(N)]

for i in range(num): #n번째 별
    start = 0 + 2*i
    end = N - 2*i-1
    for j in range(0 + 2*i, N - 2*i):
        array[start][j]='*'
        array[end][j]='*'
        array[j][start]='*'
        array[j][end]='*'


for s in array :
    print("".join(s))