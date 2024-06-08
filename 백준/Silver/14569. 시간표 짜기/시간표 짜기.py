# 수업시간
N = int(input())
classTime = []
for i in range(N):
    s = list(map(int, input().split()))
    tmp = ['0'] * 51
    for j in range(1,s[0] + 1):
        tmp[s[j] ] = '1'
    tmp = "".join(tmp)
    classTime.append(tmp)

# ~공강시간 (공강시간에 0)
M = int(input())
students = []
for i in range(M):
    s = list(map(int, input().split()))
    tmp = ['1'] * 51
    for j in range(1,s[0] + 1):
        tmp[s[j] ] = '0'
    tmp = "".join(tmp)
    students.append(tmp)

# 수업시간 & 학생 수업시간 == 0 => ok
for i in range(M): # 학생
    cnt = 0
    for j in range(N): # 수업
        s = int(students[i],2)
        c = int(classTime[j],2)
        if s & c == 0 :
            cnt += 1
    print(cnt)
        