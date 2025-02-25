str1 = input()
str2 = input()
len1= len(str1)
len2 = len(str2)


mtx = [[[0,""] for _ in range(len1+1)] for _ in range(len2+1)]

for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        if (str2[i-1]==str1[j-1]):
            mtx[i][j][0] = mtx[i-1][j-1][0] + 1
            mtx[i][j][1] = mtx[i-1][j-1][1] + str1[j-1]
        else:
            mtx[i][j][0] = max(mtx[i-1][j][0],mtx[i][j-1][0])
            if mtx[i-1][j][0] > mtx[i][j-1][0]:
                mtx[i][j][1] = mtx[i-1][j][1]
            else:
                mtx[i][j][1] = mtx[i][j-1][1] 
                
lcs = mtx[len2][len1][0]
print(lcs)
if lcs != 0:
    print(mtx[len2][len1][1])