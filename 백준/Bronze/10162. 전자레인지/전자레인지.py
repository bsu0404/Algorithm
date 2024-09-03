n = int(input())

times = [300, 60 ,10]

if n%times[2] !=0: 
    print(-1)
    exit()

a = n // times[0]
n %= times[0] 

b = n // times[1]
n %= times[1] 

c = n // times[2]
n %= times[2] 

print(a, b, c)
