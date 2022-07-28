candi_pedro = 0
candi_patrick = 0
candi_joao = 0



print("ELEIÇÃO - 2022")
candidato = str(input("digite o numero do seu candidato: "))

while(candidato != "fim"): 
    if candidato == '1':
        candi_pedro += 1
    else:
        if candidato == '2':
            candi_patrick += 1
        else:
            if candidato == '3':
                candi_joao += 1
            else:
                
                candidato = str(input("Digite o numero do seu candidato"))
                if candidato == "fim":
                    break

print("RESULTADO DAS ELEICÕES DE 2022")
print("O candidato Pedro teve {} Votos".format(candi_pedro))
print("O candidato Pedro teve {} Votos".format(candi_patrick))
print("O candidato Pedro teve {} Votos".format(candi_joao))

       