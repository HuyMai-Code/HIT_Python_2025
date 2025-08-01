n = int(input())
m = int(input())
list = []
print("Nhap mang: ")
for i in range(n):
    x = int(input())
    list.append(x)

setA = set()
setB = set()
print("Nhap setA: ")
for i in range(m):
    x = int(input())
    setA.add(x)
print("Nhap setB: ")
for i in range(m):
    x = int(input())
    setB.add(x)

happy = 0
for i in list:
    if i in setA:
        happy += 1
    elif i in setB:
        happy -= 1
    
print("Chi so hanh phuc: ", happy)