import os
from time import sleep
from colorama import Fore, Style
red = Fore.RED
gre = Fore.GREEN
yel = Fore.LIGHTYELLOW_EX
blu = Fore.CYAN
gre2 = Fore.LIGHTGREEN_EX
sty = Style.RESET_ALL

while True:
    os.system('cls')
    print(yel+'##{:#^25}'.format('')+sty)
    print('{1} 1 - {0:<20}{1}'.format('Maior e Menor', yel+'#'+sty))
    print('{1} 2 - {0:<20}{1}'.format('Positivo e Negativo', yel+'#'+sty))
    print('{1} 3 - {0:<20}{1}'.format('Vogal e Consoante', yel+'#'+sty))
    print('{1} 4 - {0:<20}{1}'.format('Turno de Estudo', yel+'#'+sty))
    print('{1} 5 - {0:<20}{1}'.format('Reajuste Salarial', yel+'#'+sty))
    print(yel+'##{:#^25}'.format('')+sty)
    print()
    while True:
        try:
            inf = int(input('Digite uma dessas opções:\n'))
        except Exception as erro:
            print(red + 'Digite apenas Numeros' + sty)
        else:
            break
    os.system('cls')
    if inf == 1:
        while True:
            num1 = input('Digite um número: ')
            num2 = input('Digite um número: ')
            n1 = (num1.replace('.', '').isdigit())  # True
            n2 = (num2.replace('.', '').isdigit())  # True
            if n1 == True and n2 == True:
                if float(num1) > float(num2):
                    print('O número {} é {}'.format(
                        red+num1+sty, gre+'MAIOR'+sty))
                elif float(num2) > float(num1):
                    print('O número {} é {}'.format(
                        red+num2+sty, gre+'MAIOR'+sty))
                else:
                    print('Os números {} e {} são {}'.format(
                        red+num1+sty, red+num2+sty, gre+'IGUAIS'+sty))
                sn = input('Deseja continuar s/n:')
                os.system('cls')
                if sn == 'n':
                    break
            else:
                print(red+'Apenas Números'+sty)
    if inf == 2:
        while True:
            n1 = float(input('Digite um número:'))
            if n1 > 0:
                print('O número {} é {}'.format(
                    red+str(n1)+sty, gre+'POSITIVO'+sty))
            elif n1 == 0:
                print('O número {} é {}'.format(red+str(n1)+sty,blu+'NULO'+sty))
            elif n1 < 0:
                print('O número {} é {}'.format(
                    red+str(n1)+sty, red+'NEGATIVO'+sty))
            sn = input('Deseja Continuar s/n:')
            os.system('cls')
            if sn == 'n':
                break
    if inf == 3:
        while True:
            vog = ['A', 'E', 'I', 'O', 'U']
            vog2 = ['a', 'e', 'i', 'o', 'u']
            vg = input('Digite uma letra:')
            if vg in vog or vg in vog2:
                print('A letra {} é uma {}'.format(
                    red+vg+sty, gre+'VOGAL'+sty))
            elif vg.isnumeric() or vg == '' or vg == ' ':
                os.system('cls')
                print(red+'Digite apenas letras'+sty)
                print()
            else:
                print('A letra {} é uma {}'.format(
                    red+vg+sty, gre+'CONSOANTE'+sty))
            sn = input('Deseja Continuar s/n:')
            os.system('cls')
            if sn == 'n':
                break
    if inf == 4:
        while True:

            nome = input('Olá, qual o seu nome?\n')
            os.system('cls')
            for i in range(4):
                print('.'*i, end='')
                sleep(0.6)
                print('   ', end='\r')
            sleep(1)
            print(yel+'##{:#^25}'.format('')+sty)
            print('{1} M - {0:<20}{1}'.format('Matutino', yel+'#'+sty))
            print('{1} V - {0:<20}{1}'.format('Vespertino', yel+'#'+sty))
            print('{1} N - {0:<20}{1}'.format('Noturno', yel+'#'+sty))
            print(yel+'##{:#^25}'.format('')+sty)
            print()
            print('Olá {}, em que {} você estuda?'.format(
                red+nome+sty, gre+'TURNO'+sty))
            print()
            tur = input('Digite a letra:')
            t = ['m', 'v', 'n', 'M', 'N', 'V']
            if tur not in t:
                print()
                print(red+"Valor Invalido"+sty)
                sleep(1)
                os.system('cls')
            else:
                print()
                if tur.upper():
                    print('{},tenha um {}'.format(
                        red+nome+sty, gre+'BOM DIA!!!!'+sty))
                if tur.upper() == 'V':
                    print('{},tenha uma {}'.format(
                        red+nome+sty, gre+'BOA TARDE!!!!'+sty))
                if tur.upper() == 'N':
                    print('{},tenha uma {}'.format(
                        red+nome+sty, gre+'BOA NOITE!!!!'+sty))

                print()
                sn = input('Deseja Continuar s/n:')
                os.system('cls')
                if sn == 'n':
                    break
    if inf == 5:
        while True:
            try:
                slr = float(input('Salário do colaborador: '))
            except Exception as erro:
                os.system('cls')
                print(red+'Apenas Numeros'+sty)
                sleep(1.5)
                os.system('cls')
            else:
                if (slr <= 280):
                    perc = 20
                elif (slr <= 700):
                    perc = 15
                elif (slr <= 1500):
                    perc = 10
                else:
                    perc = 5

                print('Salario original: R$ {}'.format(blu+str(slr)+sty))
                print('Percentual: {}{} {}'.format(
                    blu+str(perc)+sty, blu+'%'+sty, gre+'⬆'+sty))

                perc = perc/100.0
                aum = round((perc * slr),2)
                nov_slr = slr + aum

                print('Aumento: R$ {} {} '.format(
                    blu+str(aum)+sty, gre+'⬆'+sty))
                print('Novo salário: R$ {} '.format(
                    blu+str(nov_slr)+sty, gre+'⬆'+sty))
                print()
                sn = input('Deseja Continuar s/n:')
                os.system('cls')
                if sn == 'n':
                    break
    sn2 = input(blu+'Deseja Voltar para {} (s/n)\n'.format(red+'Tela inicial?'+sty)+sty)
    if sn2 == 'n':
        os.system('cls')
        print(gre2+'FIM DO PROGRAMA'+sty)
        sleep(1.5)
        os.system('cls')
        break
