s = input()
cnt = 1
while s[0]!="-":
    arr = []
    for i in range(len(s)):
        if arr and arr[-1] == "{" and s[i] == "}":
            arr.pop()
        else:
            arr.append(s[i])
            
    ans = 0
    for i in range(0,len(arr),2):
        if arr[i]=="}" and arr[i+1] == "{":
            ans += 2
        else:
            ans += 1


    print("%d. %d" %(cnt, ans))
    s = input()
    cnt += 1

    