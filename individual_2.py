x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

val1 = (x ** 2) * y
val2 = x * (y **2)
if val1 > val2:
    max_val = val1
elif val2 > val1:
    max_val = val2

val3 = x - y
val4 = x + 2 * y
if val3 < val4:
    min_val = val3
elif val4 < val3:
    min_val = val4

U = (max_val ** 2) + (min_val ** 2)

print (f"Значение U = {U}")