str = input()
ans = 0

alpabet=[3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

for s in str:
    ans += alpabet[ord(s)-ord("A")]

print(ans)
