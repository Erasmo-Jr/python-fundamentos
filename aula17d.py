a = [2, 3, 4, 7]
b = a
b[2] = 8 #Essa substituição não afetara somente a lista b, mas também a lista a, agindo ATALHO e não de CÓPIA
print(f'Lista A: {a}')
print(f'Lista B: {b}')