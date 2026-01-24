galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1]) #Indentificando por posições de lista dentro de lista

for p in galera: #Para cada pessoa 'p' em galera
    print(p[0]) #Filtrando somente as posições 0
    #ou pode fazer formatado
    print(f'{p[0]} tem {p[1]} anos de idade.')