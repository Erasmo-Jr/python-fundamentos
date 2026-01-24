pessoas = {'nome': 'Erasmo', 'sexo': 'M', 'idade': 23}
del pessoas['sexo']#apagando a chave sexo
pessoas['nome'] = 'Junior' #Substituindo nomes
pessoas['peso'] = 82.2 #Adicionando itens(chave e valor)
for k in pessoas.keys(): #Mostrando todas as chaves
    print(k)
for k in pessoas.values(): #Mostando todos os valores
    print(k)
for k, v in pessoas.items(): #Mostrando todos os itens (chaves e valores) formatado
    print(f'{k} = {v}')