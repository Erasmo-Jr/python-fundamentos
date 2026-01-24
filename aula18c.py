print('~~'*5, end='')
print(' Maiores e Menores de Idade ', end='')
print('~~'*5)

maior = menor = 0
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Copiando a lista dados em galera
    dado.clear() #Apagando lista dados
print('-=' * 30)
for p in galera: #Para pessoas (p) em lista galera
    print(f'{p[0]} tem {p[1]} anos')
print('-=' * 30)
for p in galera:
    if p[1] > 18: #Mostra pessoas da lista é maior de 18 anos
        maior += 1
        print(f'{p[0]} com {p[1]} anos É maior de idade')
    else: #caso não seja
        print(f'{p[0]} tem {p[1]} anos portanto NÃO é maior de idade')
        menor += 1
print('-=' * 30)
if menor == 0:
    print('Não tem pessoas menores de idade')
elif menor == 1:
    print(f'Temos {menor} pessoa menor de idade')
else:
    print(f'Temos {menor} pessoas menores de idade')
if maior == 0:
    print('Não tem pessoas maiores de idade')
elif maior == 1:
    print(f'Temos {maior} pessoa maior de idade')
else:
    print(f'Temos {maior} pessoas maiores de idade')
