k = int(input("Nhap K: "))
a = []

for i in range(k):
    x = int(input())
    a.append(x)

n = int(input("Nhap so dong cua ma tran: "))
m = int(input("Nhap so cot cua ma tran: "))

matrix = []
tmp = []

if n * m > k:
    print("NO")
else:
    for i in range(n * m):
        tmp.append(a[i])
        if len(tmp) == m:
            matrix.append(tmp)
            tmp = []

print()
print(matrix)
