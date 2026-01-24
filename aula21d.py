def funcao():
    n1 = 4 #N1 Escopo local
    print(f'N1 dentro vale {n1}')

n1 = 2 #Escopo Global
funcao()
print(f'N1 fora vale {n1}')