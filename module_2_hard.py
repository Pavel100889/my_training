print('Введите число на первой табличке:')
a = int(input())
password = []
n = 1
for i in range(1, 20):
    for j in range(n, 20):
        if i == j:
            continue
        if a % (i + j) == 0:
            password.append(i)
            password.append(j)
            n += 1
print("".join(map(str, password)))


