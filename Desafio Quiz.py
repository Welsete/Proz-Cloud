respcerto = 0
resperrado = 0

def conferir():
    while True:
        conferencia = input(f"Deseja continuar? [S][N]")
        if conferencia == "N":
            exit()
        elif conferencia == "S":
            break

def perguntas():
    global respcerto,resperrado
    while True:
        try:
            r1 = int(input("Quanto é 2+2?"))
            if r1 == 4:
                print("Você acertou")
                respcerto += 1
            else:
                print("Errado!")
                resperrado += 1
                conferir()

            r2 = int(input("Quanto é 2+3?"))
            if r2 == 5:
                print("Você acertou")
                respcerto += 1
            else:
                print("Errado!")
                resperrado += 1
                conferir()

            r3 = int(input("Quanto é 2+4?"))
            if r3 == 6:
                print("Você acertou")
                respcerto += 1
            else:
                print("Errado!")
                resperrado += 1
                conferir()

            r4 = int(input("Quanto é 2+5?"))
            if r4 == 7:
                print("Você acertou")
                respcerto += 1
            else:
                print("Errado!")
                resperrado += 1
                conferir()

            r5 = int(input("Quanto é 2+6?"))
            if r5 == 8:
                print("Você acertou")
                respcerto += 1
            else:
                print("Errado!")
                resperrado += 1
                conferir()

            r6 = int(input("Quanto é 2+7?"))
            if r6 == 9:
                print("Você acertou")
                respcerto += 1
            else:
                print("Errado!")
                resperrado += 1
                conferir()
        except ValueError:
            print("Siga as intruções")
            perguntas()
        break

def quantidadeae (respcerto,resperrado):
    if respcerto >= 4:
        print ("Aprovado")
    else:
        print ("Reprovado")

perguntas()
quantidadeae(respcerto,resperrado)
print(respcerto)