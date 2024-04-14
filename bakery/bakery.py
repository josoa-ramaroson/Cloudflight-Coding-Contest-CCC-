john_delivering_str = input().split("F ")
day_sales = list(map(str.split,john_delivering_str[1:-1]))
payment_bank = list(map(str.split, john_delivering_str[-1].split("B ")))
day_sales.append(payment_bank.pop(0))

for day in range(len(day_sales)):
    if day_sales[day][1] != payment_bank[day][1]:
        print(day_sales[day][0], end=" ")
print()