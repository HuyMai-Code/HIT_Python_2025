n = int(input("N = "))

count = 0
sum = 0

while (n > 0):
    sum += n % 10
    n = (int)(n / 10)
    count += 1

print(f"Số chữ số: {count} Tổng chữ số: {sum}")