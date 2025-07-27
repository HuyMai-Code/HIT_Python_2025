name = input()

name = name.lower()

name_result = ""
tmp = 0
a = 0
for char in name:
    if tmp == 1 or a == 0:
        name_result += char.upper()
        tmp = 0
        a = 1
        continue
    name_result += char
    if char == " ":
        tmp = 1
    
print(name_result)