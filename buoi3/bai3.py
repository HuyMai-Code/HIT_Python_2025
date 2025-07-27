s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")


print(f"Dao nguoc s1: {s1[::-1]}")

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

s2_ = s2[b-1:a-2:-1]

print(f"Chuoi s2 sau khi dao nguoc tu vi tri a -> b: {s2.replace(s2_[::-1], s2_)}")

s3 = ""
for i in range(0, len(s1)):
    if i % 2 == 1:
        s3 += s1[i]

print(f"S3: {s3}")

i = 0
j = 0
s4 = ""
while i < len(s1) and j < len(s2):
    s4 += s1[i]
    s4 += s2[j]
    i += 1
    j += 1

while i < len(s1):
    s4 += s1[i]
    i += 1

while j < len(s2):
    s4 += s2[j]
    j += 1

print(f"S4 dan xen cac ki tu cua s1 va s2: {s4}")