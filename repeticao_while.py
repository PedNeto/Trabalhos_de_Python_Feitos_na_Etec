#x = 1
#while x <= 15:
    #print(x)
    #x = x + 1

quantidade = 0
soma = 0
media = 0

valor = float(input('Digite um valor: '))
while valor > 0.0:
    soma = soma + valor
    quantidade = quantidade + 1
    
    valor = float(input('Digite um valor: '))
    media = soma / quantidade 
    print('\n Total da Soma =', soma)
    print('\n Quantidade de Valores =', quantidade)
    print('\n Média dos Valores =', media)
    