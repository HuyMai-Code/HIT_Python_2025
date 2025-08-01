n = int(input("Nhap n: "))

a = []
for i in range(n):
    x = input()
    a.append(x)

b = tuple(a)
print(b)
cnt = 0
for i in b:
    if i.isdigit():
        cnt += 1
print("So luong phan tu co dang so la: ", cnt)