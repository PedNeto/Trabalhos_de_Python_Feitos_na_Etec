def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas números válidos.\033[m')
        if ok:    
            break
    return valor
    
n = leiaInt('Numero: ')
print (f'o numero digitado foi {n}')
        