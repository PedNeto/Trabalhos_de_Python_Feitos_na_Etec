import os
from colorama import Fore
from colorama import Style

#pip install colorama
#usar o "pip" no cmd para instalar bibliotecas que não estão instalados

os.system('cls')

def soma(n1, n2):
    resposta = n1 + n2
    print("A soma é {}".format(resposta))
    
def sub(n1, n2):
    resposta = n1 - n2
    print("A subtração é {}".format(resposta))

def div(n1, n2):
    if n2 == 0:
        print()
        print(Fore.RED + Style.BRIGHT + "NÃO EXISTE DIVISÃO POR ZERO" + Style.RESET_ALL)
    else:
        resposta = n1 / n2  
        print("A subtração é {}".format(resposta))


n1 = int(input("Digite 1° número: "))
n2 = int(input("Digite 2° número: "))

#soma(n1,n2)
#sub(n1,n2)
div(n1,n2)

print()


