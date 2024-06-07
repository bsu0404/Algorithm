N = int(input())
K =int(input(),2)
cnt = 0
while K != 0:
    K = K-(K&((~K)+1))
    cnt += 1
print(cnt)