def realizar_operacao(numero1, numero2, operacao):
    if operacao == '1':
        resultado = numero1 + numero2
        print("A soma de {} com {} é igual a: {}".format(numero1, numero2, resultado))
    elif operacao == '2':
        resultado = numero1 - numero2
        print("A subtração de {} por {} é igual a: {}".format(numero1, numero2, resultado))
    elif operacao == '3':
        resultado = numero1 * numero2
        print("A multiplicação de {} por {} é igual a: {}".format(numero1, numero2, resultado))
    elif operacao == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print("A divisão de {} por {} é igual a: {}".format(numero1, numero2, resultado))
        else:
            print("Erro: Divisão por zero!")

def calculadora():
    while True:
        print("Calculadora")
        print("Bem vindo a Calculadora")
        print("Opções:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")

        operacao = input("Digite o número para a operação correspondente: ")

        if operacao == '0':
            print("Encerrando a calculadora. Até mais!")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Essa opção não existe. Tente novamente.")
            continue

        try:
            numero1 = float(input("Digite o Primeiro Numero: "))
            numero2 = float(inpu3t("Digite o Segundo Numero: "))
        except:
            print("Erro: Insira valores numéricos válidos.")
            continue

        realizar_operacao(numero1, numero2, operacao)

        continuar = input("Deseja realizar outra operação? (S para Sim, qualquer outra tecla para sair): ")
        if continuar.upper() != 'S':
            print("Encerrando a calculadora. Até mais!")
            break

calculadora()
