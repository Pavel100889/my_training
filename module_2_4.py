numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
primes = []
not_primes = []
numbers.remove(1)
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)
print ('Primes:', primes)
print('Not primes:', not_primes)