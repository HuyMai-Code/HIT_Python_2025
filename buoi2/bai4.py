n = int(input("Số xu: "))

beer = (int)(n / 28)
a = beer
while (a % 3 == 0):
    a = (int)(a / 3)
    beer += a


print(f"Số chai bia có thể mua được là: {beer}")
