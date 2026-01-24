num = [2, 5, 9, 1]
num[2] = 3 #Substituindo elementos da lista
num.append(7) #Incluindo um elemento
num.sort(reverse=True) #Deixando em ordem reversa
num.insert(2, 0) #Na posição 2 inserindo Número 0
num.pop() #Elimina última elemento da última posição
num.pop(2) #Eliminando elemento na posição 2
num.remove(2) #Elimina o PRIMEIRO elemento 2 (Não é a posição)
if 4 in num: #Se o elemento 4 estiver na lista (número)
    num.remove(4) #Remover elemento 4
else: #Se não
    print('Não achei o número 4') #Imprimir essa mensagem
print(num) #Imprimindo listas
print(f'Essa lista tem {len(num)} elementos.') #Imprimindo quantidade elementos da lista