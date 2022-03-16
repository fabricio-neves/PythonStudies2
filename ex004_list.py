lista = [2, 4, 7, 5, 4, 2, 6, 8, 4, 2, 5, 3]
listb = []
for l1 in lista:
    if l1 not in listb:
        listb.append(l1)
print(listb)

'''
next = 0
print(len(lista))

for previous in lista:
    next += 1
    while next < len(lista):
        if previous == lista[next]:
            lista.pop(next)
            print(f'{lista[next]} was removed.')
            next = next - 1
print(lista)
'''
