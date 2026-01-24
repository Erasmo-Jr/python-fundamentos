#Forma correta de usar COPIA de listas e NÃO ATALHOS
a = [2, 3, 4, 7]
b = a[:] #Usando esse fatiamento de string ele faz a cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')