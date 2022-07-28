import pygame
import os
import time

def som():
    pygame.mixer.init()
    pygame.mixer.music.load('E:/Aula_Programação_e_ Algoritimo_Edson/urna.mp3')
    pygame.mixer.music.play()
    time.sleep(1)

def tela():
    os.system('cls')
    
cand1 = 0
cand2 = 0
cand3 = 0

for n in range(3):
    print('1 : Junin')
    print('2 : Pedrin')
    print('3 : Junin')
    opcao = int(input('ESCOLHAS UMA DA OPCAO ACIMA : '))
    if opcao > 3:
        print(f'OPCAO INVALIDA')
        exit()
    if opcao == 1:
        cand1 = cand1 + 1
    elif opcao == 2:
        cand2 = cand2 + 1
    elif opcao == 3:
        cand3 = cand3 + 1
    
    som()
    tela()  
        
    
print('O PRIMEIRO CANDIDATO OBTEVE,', cand1 , 'votos')
print('O SEGUNDO CANDIDATO OBTEVE,', cand2 , 'votos')
print('O TERCEIRO CANDIDATO OBTEVE,', cand3 , 'votos')



    

    