from funções_úteis.limpeza_terminal import clear

def editarAintensidade(intensidade_antiga):
    while True:

        entrada = input(f"A intensidade atual é: {intensidade_antiga}\n"
            "Para permanecer com a mesma intensidade clique ENTER\n\n"
            "[1] LEVE\n"
            "[2] MODERADO\n"
            "[3] PESADO\n\n"
            "Digite a intensidade: "
        )

        if entrada == "": #se estiver em branco é porque foi apertado ENTER e continua o antigo
            return ""

        try:
            intensidade = int(entrada)

            match intensidade:

                case 1:
                    return "Treino Leve"

                case 2:
                    return "Treino Moderado"

                case 3:
                    return "Treino Pesado"

                case _:
                    clear()
                    print("Digite apenas 1, 2 ou 3!\n")

        except ValueError:
            clear()
            print("Resposta inválida!\n")