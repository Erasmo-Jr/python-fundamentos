valores = []
valores.append(5)
valores.append(9)      #incluindo valores na lista
valores.append(4)

for v in valores: #Para cada v(valor) em valores
    print(f'{v}...', end='')

for c, v in enumerate(valores): #Para cada c(contador, posição) e v(valor) está enumerado
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')