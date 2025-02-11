def getDisjoint(targetNum):
    disjoint = set()
    num = targetNum

    for i in range(2,int(num**(1/2) + 1)):
        if targetNum % i == 0:
            while targetNum % i == 0:
                targetNum /= i
            disjoint.add(i)
    # 제곱근 이상은 1개 이상일 수 없음
    if targetNum > 1:
        disjoint.add(targetNum)
    return disjoint


# main
N = int(input())

# 서로소 집합
disjoint = getDisjoint(N)
# 오일러 피 공식
for i in disjoint:
    N *= (1-(1/i))
print(int(N))
