input_number = int(input())


primes = []
primes.append([0])
primes.append([2, 3, 5, 7])

def is_prime(num):
    if num == 1:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True


for i in range(2, 9) :
    new_primes = []
    for prime in primes[i - 1] :
        tmp = prime * 10
        for j in range(1, 10, 2) :
            new_tmp = tmp + j
            if (is_prime(new_tmp)) :
                new_primes.append(new_tmp)
    primes.append(new_primes)

for dec in primes[input_number] :
    print(dec)

