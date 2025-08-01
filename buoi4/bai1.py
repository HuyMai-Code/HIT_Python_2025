a = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

new_tuple = []

for i in a:
    new_tuple.append(int(i))

new_tuple = tuple(new_tuple)
print(new_tuple)

sum = 0
count = 0
for i in new_tuple:
    sum += i
    count += 1
print(f"Trung binh cong cac phan tu trong tuple: {sum/count}")
