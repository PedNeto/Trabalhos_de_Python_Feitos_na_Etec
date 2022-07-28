ehNumero = False
ehNumero2 = False

while (ehNumero == False):
    chute = input("Digite o seu número: ")
    chute2 = input("Digite o seu número: ")    

    try:
        int(chute)
        print("O chute é um número!")
        ehNumero = True

    except ValueError:
        try:
            float(chute)
            print("O chute é um número!")
            ehNumero = True

        except ValueError:
            print("O valor não é um número")
            
            ehNumero = False
        continue
    try:
        int(chute2)
        print("O chute2 é um número!")
        ehNumero2 = True

    except ValueError:
        try:
            float(chute2)
            print("O chute2 é um número!")
            ehNumero2 = True

        except ValueError:
            print("O valor não é um número")
            
            ehNumero2 = False
       


    


