str = input()
l = len(str)
arr = [0] * 26
for i in range(l):
    s = str[i]
    j = ord(s) - 65
    arr[j] += 1

cnt = 0
ans = ""
tmpC = "."
for i in range(26):
    c =chr(i+65)
    if arr[i] % 2 == 1:
        tmpC = c
        cnt += 1
    if cnt > 1:
       ans = "."
       break
    for _ in range(arr[i]//2):
        ans += c
if ans == ".":
    print("I'm Sorry Hansoo")
elif tmpC != ".":
    print(ans +tmpC+ ans[::-1])
else:
    print(ans + ans[::-1])
