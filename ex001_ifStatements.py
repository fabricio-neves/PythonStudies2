price = 10 ** 6
has_good_credit = True
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f'Down price is ${down_payment}')
