prices = [10, 20, 30]
total = 0
for price in prices:
    total = total + price
print(total)

numbers = [5, 2, 5, 2, 2]
i = 0
printer = ""
for row in numbers:
    for column in range(numbers[i]):
        print('x', end='')
    print(printer)
    printer = ""
    i += 1
