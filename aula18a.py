teste = list()
teste.append('Gustavo') #incluindo na lista teste
teste.append(40) #incluindo na lista teste
galera = list()
galera.append(teste[:]) #Incluindo a lista teste na lista galera COPIANDO com [:]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)