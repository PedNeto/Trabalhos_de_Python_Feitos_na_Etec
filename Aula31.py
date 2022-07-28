nome = 'Pedro'

n1 = float(input('Digite a Pimeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))

med = (n1 + n2)/2
while True:
    if n1 >=11:
        print('nsei')
    else:   
        print('') 
        break

if med >= 5:
    print('O aluno {} foi APROVADO!!'.format(nome))
elif med <= 4:
    print('O aluno {} ficou RECUPERAÇÃO'.format(nome))
