""""""""

tickets = int(input('Введите количество билетов:'))
qt_tickets = tickets
ages = []
i = 1
while tickets:
    visitor_age = int(input(f'Введите возраст посетителя № {i}:'))
    i += 1
    tickets -= 1
    ages.append(visitor_age)
total_price = 0
for age in ages:
    if 18 <= age < 25:
        total_price += 990
    if age >= 25:
        total_price += 1390
    if age < 18:
        total_price += 0
if qt_tickets > 3:
    total_price *= 0.9
    print("Цена со скидкой 10% =", total_price)
else:
    print(f"Цена за {i-1} билетов = ", total_price)
