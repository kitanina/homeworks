per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent = list[float](per_cent.values())
money = float(input('Enter the sum you want to deposit:')) / 100

for i, value in enumerate(per_cent):
    per_cent[i] = value * money
deposit = per_cent
print(deposit)
print('The max sum you could earn:', max(deposit))

