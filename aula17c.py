valores = list()
for cont in range(0, 5): #Quando laço de repetição cont(contador) estiver no intervalor entre 0 á 5:
    valores.append(int(input('Digite um valor: '))) #Incluindo valores com append e solicitando valor a ser digitado com input

for c, v in enumerate(valores): #Para cada c(contador, posição) e v(valor) está enumerado
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')