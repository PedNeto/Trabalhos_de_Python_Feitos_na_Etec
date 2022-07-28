def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            valor = int(n1)
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas números válidos.\033[m')
        if ok:
            break
    return valor


print('***************')
print('*             *')
print('* CALCULADORA *')
print('*             *')
print('***************')
print()

n1 = leiaInt('Digite o 1° numero: ')
n2 = leiaInt('Digite o 2° numero: ')
print()

print('operadores aritmeticos: \n+ : Adição \n- : Subtração \n* : Multiplicação \n/ : Divisão')
print()
ope = input('Digite o operador:')
print()
res = int

if ope == '/' and n2 == 0:
    print('NÃO EXISTE DIVISÃO POR ZERO')
    print()
elif ope == '+':
    res = n1 + n2
    print(f'O resultado de {n1} + {n2} é {res}')
    print()
elif ope == '-':
    res = n1 - n2
    print(f'O resultado de {n1} - {n2} é {res}')
    print()
elif ope == '*':
    res < - n1 * n2
    print(f'O resultado de {n1} * {n2} é {res}')
    print()
elif ope == '/':
    res = n1 / n2
    print(f'O resultado de {n1} / {n2} é {res}')
    print()
