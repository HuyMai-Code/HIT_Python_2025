# Bài 2: Tìm hiểu trước kiến thức buổi 2

## 1. Các kiểu dữ liệu trong Python

- `int`: Số nguyên (ví dụ: `5`, `-10`, `0`)
- `float`: Số thực (ví dụ: `3.14`, `-2.5`)
- `str`: Chuỗi ký tự (ví dụ: `"Hello"`, `'Python'`)
- `bool`: Kiểu logic (`True`, `False`)
- `list`: Danh sách (ví dụ: `[1, 2, 3]`)
- `tuple`: Bộ (ví dụ: `(1, 2, 3)`)
- `dict`: Từ điển (ví dụ: `{"name": "Huy", "age": 18}`)
- `set`: Tập hợp (ví dụ: `{1, 2, 3}`)

---

## 2. Các toán tử trong Python

- **Toán tử số học**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Toán tử so sánh**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Toán tử logic**: `and`, `or`, `not`
- **Toán tử gán**: `=`, `+=`, `-=`, `*=`, `/=`, ...
- **Toán tử membership**: `in`, `not in`
- **Toán tử identity**: `is`, `is not`

---

## 3. Mệnh đề điều kiện và vòng lặp

### Mệnh đề điều kiện (`if`, `elif`, `else`):

```python
if a > 0:
    print("a là số dương")
elif a == 0:
    print("a bằng 0")
else:
    print("a là số âm")
```
### Vòng lặp for:

```python
for i in range(5):
    print(i)
```
### Vòng lặp while:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```
## 4. Kiểu dữ liệu True và False (kiểu bool)

- `True`: đại diện cho giá trị đúng (1)
- `False`: đại diện cho giá trị sai (0)
### Ví dụ:
```python
x = 5
print(x > 3)   # True
print(x == 10) # False
```
Các giá trị sau sẽ được xem là False trong điều kiện:
- `0`, `0.0`
- `""` (chuỗi rỗng)
- `[]`, `()`, `{}` (danh sách, tuple, dict rỗng)
- `None`