a = {"001", "003", "002", "007"}
b = {"003", "005", "004", "001"}

print("Danh sach ma sinh vien dang ki TA tai ban tiep nhan so 1: ", a)
print("Danh sach ma sinh vien dang ki TA tai ban tiep nhan so 2: ", b)
r = a.intersection(b)
if r == set():
    print("Khong co sinh vien nao dang ky hoc tai ca 2 ban")
else:
    print("Cac sinh vien co ma sinh vien dang ki hoc tai ca 2 ban: ", end = "")
    for i in r:
        print(i, end = "  ")
print()
r1 = a.copy()
for i in b:
    r1.add(i)
print("Danh sach tong hop cua cac sinh vien da dang ki cua ca 2 ban: ", r1)

for i in r:
    a.discard(i)
print("Danh sach cac sinh vien da dang ky tai ban 1 ma khong dang ky tai ban 2: ", a)