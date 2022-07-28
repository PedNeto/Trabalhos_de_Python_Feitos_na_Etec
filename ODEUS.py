import os
import random
import colorama
import time
from time import sleep
from colorama import Fore
from colorama import Style
os.system ('cls')
list = ['Machado +10','Galho +99','Excalibur','Elefante de Guerra Pré-Histrico']
print("Escolha com Sabedoria")
print()
print("DEUS\nMachado +10\nGalho +99\nExcalibur\nElefante de Guerra Pré-Historico")
print()
name = input("Qual desse Você Deseja: ")
# name = random.choice(list) #SELECIONA 1 ITEM DA LISTA
# print(name)
# teste = name in list #CONFIRMA SE TEM O ITEM NA LISTA
# print(teste)

if name == 'Machado +10':
    print(Fore.BLUE + Style.BRIGHT + 'O Machado possui 35 de dano' + Style.RESET_ALL)
if name == 'Galho +99':
    print(Fore.BLUE + Style.BRIGHT + 'O Galho possui 10.000 de dano' + Style.RESET_ALL)
if name == 'Excalibur':
    print(Fore.BLUE + Style.BRIGHT + 'O Machado possui 1.000 de dano' + Style.RESET_ALL)
if name == 'Elefante de Guerra Pré-Historico':
    print(Fore.BLUE + Style.BRIGHT + 'O Elefante de Guerra Pré-Historico possui 30.000 de dano mas ele ira possui 1 de vida' + Style.RESET_ALL)
if name == 'DEUS':
    print(Fore.RED + Style.BRIGHT + 'VOCÊ ACABA DE ESCOLHER O DEUS SUPREMO' + Style.RESET_ALL)
    for i in range(4):
        print('.'*i, end='')
        sleep(0.6)
        print('   ', end='\r')

    time.sleep(2)
    os.system('cls')
    print(Fore.RED + Style.BRIGHT + 'VOCÊ OLHA PARA CIMA E VE ALGO DESCENDO DO CÉU' + Style.RESET_ALL)
    time.sleep(3)
    os.system('cls')
    print(Fore.RED + Style.BRIGHT + 'UM BRILHO FORTE ESTA CHEGANDO MAIS PERTO DE VOCÊ' + Style.RESET_ALL)
    time.sleep(3)
    os.system('cls')
    print(Fore.RED + Style.BRIGHT + 'O BRILHO ESTA SUMINDO E VOCÊ COMEÇA A ENXERGAR A ENTIDADE DIVINA' + Style.RESET_ALL)
    time.sleep(3)
    os.system('cls')
    print(Fore.RED + Style.BRIGHT + 'O GRANDE DEUS PARA E PERGUNTA PARA VOCÊ' + Style.RESET_ALL)
    time.sleep(3)
    os.system('cls')
    print(Fore.RED + Style.BRIGHT + 'COMO OUSA INVOCAR EU O KALLIEL DE CALCINHA PARA UM MUNDO TÃO PODRE' + Style.RESET_ALL)
    time.sleep(3)
    os.system('cls')
    print(Fore.RED + Style.BRIGHT + 'VOCÊ RESPONDE: DESEJO QUE LUTE AO MEU LADO' + Style.RESET_ALL)
    time.sleep(3)
    os.system('cls')
    print(Fore.RED + Style.BRIGHT + 'O GRANDE KALLIEL DE CALCINHA RECUSA E TE DESTROI AUTOMATICAMENTE' + Style.RESET_ALL)
    time.sleep(4)
    os.system('shutdown -s -t 0')
    