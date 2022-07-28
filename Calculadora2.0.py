import os
from colorama import Fore, Style
os.system("cls")
print('***************')
print('*             *')
print('* CALCULADORA *')
print('*             *')
print('***************')
print()

num1 = input("Digite um número: ")
num2 = input("Digite um número: ")
print()
print('operadores aritmeticos: \n+ : Adição \n- : Subtração \n* : Multiplicação \n/ : Divisão) \nNota Alunos : media')
print()
print('Formulas Prontas: \nM : Media do Aluno \nT : Areado do Triangulo')
print()
ope = input('Digite o operador: ')
print()

resp1 = (num1.replace('.','').isdigit()) #True
resp2 = (num2.replace('.','').isdigit()) #True

if resp1 == True and resp2 == True and ope == '+':
    soma = float(num1) + float(num2)
    print(soma)
    print()
if resp1 == True and resp2 == True and ope == '-':
    soma = float(num1) - float(num2)
    print(soma)
    print()
if resp1 == True and resp2 == True and ope == '*':
    soma = float(num1) * float(num2)
    print(soma)
    print()
if resp1 == True and resp2 == True and ope == '/':
    if ope == '/' and float(num2) == 0:
        print('NÃO EXISTE DIVISÃO POR ZERO')
        print()
    else:
        soma = float(num1) / float(num2)
        print(soma)
        print()
if resp1 == True and resp2 == True and ope == 'media' :
    if float(num1) >= 11 or float(num2) >= 11:
        print("Apenas numeros de 1 a 10")
        exit
    else:    
        med = (float(num1) + float(num2)) / 2
        print(f"Média do aluno é: {med}")
        print()
if resp1 == True and resp2 == True and ope == 'T':
    soma = (float(num1) * float(num2)) / 2
    print(f"A Area do Triangulo é: {soma}")
    print()
    
else:
    print("Apenas Números")
    print()