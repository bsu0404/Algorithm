s1 = input()
s2 = input()
str = []

for i in range(len(s1)):
    str.append(s1[i])

    if ''.join(str[-len(s2):]) == s2:
        for _ in range(len(s2)):
            str.pop()
        # str = str[:-len(s2)]

if len(str) == 0 :
    str = "FRULA"

print("".join(str))