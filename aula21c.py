def test():
    x = 8 #Variavel x tem escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2 #Variavel Global
print(f'No programa principal, n vale {n}')
test()
print(f'No promagra principal, x vale {x}')