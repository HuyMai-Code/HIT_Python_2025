print("1.")
n = int(input("Nhap N: "))

list = []

for i in range(n):
    a = int(input())
    list.append(a)

x = int(input("Nhap so X: "))
count = 0

for i in list:
    if (x == i):
        count += 1
print("\n2.")
print(f"So X xuat hien {count} lan trong list")

list2 = [8, 5, 4, 0, 1, 3]
j = 0

for i in range(2, 8):
    list[i] = list2[j]
    j += 1
print("\n3.")
print(f"List sau khi thay the phan tu tu 2 -> 7: {list}")

max_value = max(list)
min_value = min(list)

print("\n4.")
print(f"Gia tri lon nhat: {max_value}")
print(f"Gia tri nho nhat: {min_value}")

print("\n5.")
y = int(input("Nhap so Y: "))
list.insert(0, y)
print("Da chen Y vao list")

tang = 0
giam = 0
tmp = list[0]

for i in range(0, len(list)):
    if i == 0:
        continue
    if tmp >= list[i]:
        tang = 1
    if tmp <= list[i]:
        giam = 1
    tmp = list[i]

print("\n6.")
if tang == 0:
    print("Tang")
elif giam == 0:
    print("Giam")
elif giam == 1 and tang == 1:
    print("NO")




