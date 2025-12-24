#1-misol
n = int(input("Balandlikni kiriting: "))
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*" + " "*(n-2) + "*")

#2-miasol
n = 5
for i in range(n, 0, -1):
    for j in range(i, n+1):
        print(j, end=" ")
    print()

#3-misol
n = int(input("Qatorlar soni: "))
son = 1
for i in range(1, n+1):
    for j in range(i):
        print(son, end=" ")
        son += 1
    print()

#4-misol
son = int(input("Son kiriting: "))
teskari = 0

while son > 0:
    qoldiq = son % 10
    teskari = teskari * 10 + qoldiq
    son //= 10

print("Teskari son:", teskari)
