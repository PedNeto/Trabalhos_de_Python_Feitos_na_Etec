import os
os.system('cls')
try:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite um número: '))
    div = n1/n2
    soma = n1+n2
    mult = n1*n2
    sub = n1-n2
except Exception as erro:
    print(f'Erro encontrado foi {erro.__class__}')
if div == 1.00:
    breakpoint
else:
    print(f'O resultado é: {div:.2f}')
    print(f'O resultado é: {soma:.2f}')
    print(f'O resultado é: {mult:.2f}')
    print(f'O resultado é: {sub:.2f}')