goal, num = map(int,input().split())

ans  = 1

while goal < num:
    if num % 10 == 1:
        num //= 10
    elif num % 2 == 0:
        num /= 2
    else:
        break
    ans += 1

print(ans if num == goal else -1)