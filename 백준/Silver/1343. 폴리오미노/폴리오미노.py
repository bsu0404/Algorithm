str = input()
ans = ''
l = len(str)
i = 0
while i < l:
    if str[i] == 'X' and i + 1 < l and str[i + 1] == 'X' :
        if i + 2 < l and str[i + 2] == 'X' and  i + 3 < l and str[i + 3] == 'X':
            ans += 'AAAA'
            i += 4
        else:
            ans += 'BB'
            i += 2
    elif str[i] =='.':
        ans += '.'
        i += 1
    else:
        print('-1')
        exit()
        
print(ans)
