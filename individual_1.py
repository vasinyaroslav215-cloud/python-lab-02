if __name__ == "__main__":
    m = int(input("Введите номер месяца (от 1 до 12):"))

if 1 <= m <= 12:
    if m == 2:
        days = 28
    elif m in (4, 6, 9, 11):
        days = 30
    else:
        days = 31
        
    print(f"В месяце {m} ровно {days} дней.")
else:
    print("Ошибка! Номер месяца должен быть от 1 до 12.")
    