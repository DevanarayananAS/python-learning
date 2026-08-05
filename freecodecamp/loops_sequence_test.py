developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(ids, developers)))

for name, dev_id in zip(ids, developers):
    print(name)
    print(dev_id)


odd_num = []

for num in range(20):
    if num % 2 != 0:
        odd_num.append(num)

print(odd_num)


odd_num = [num for num in range(20) if num % 2 != 0]
print(odd_num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

results = [(num, 'odd') if num % 2 != 0 else (num, 'even') for num in numbers]

print(results)