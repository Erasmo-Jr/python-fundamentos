estado = {} #Dicionario
brasil = [] #Lista
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #Para fazer a copia de um dicionario tem quer ser feito assim
for e in brasil: #For para lista
    for k, v in e.items(): #For para dicionario
        print(f'O campo {k} tem valor {v}.') #Printando para chaves e valores
    for v in e.values(): #Metodo apenas para valores
        print(v, end=' ')
    print()