salary = int(input("Lương: "))
tax = 0
income = 0

if salary >= 15000000:
    tax = salary * 0.3
    income = salary - tax
elif salary < 7000000:
    tax = salary * 0.1
    income = salary - tax
else:
    tax = salary * 0.2
    income = salary - tax

print(f"Thuế: {tax} Thu nhập: {income}")
