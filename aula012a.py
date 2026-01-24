import emoji
from time import sleep
nome = str(input('Qual é o seu nome? '))
print('-=-'*5)
print('\033[32mPROCESSANDO...\033[m')
print('-=-'*5)
sleep(2)
if nome == 'Erasmo':
    print(emoji.emojize('Que nome bonito!:smiling_face_with_sunglasses:'))
elif nome == 'Endre' or nome == 'Rai' or nome == 'Vilian' or nome == 'Charles':
    print(emoji.emojize('Nome de jogador caro!:face_with_hand_over_mouth:'))
elif nome in 'Vegeta Goku':
    print(emoji.emojize('Nome de Guerreiro Saiyajin!!!:anguished_face:'))
else:
    print(emoji.emojize('Que nome comum!:disguised_face:'))
print('Tenha um bom dia, {}!'.format(nome))
