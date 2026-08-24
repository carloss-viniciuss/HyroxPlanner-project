from funções_úteis.limpeza_terminal import clear

def editarOtipo(tipo_antigo):
    while True:

        entrada = input(f"O tipo atual é: {tipo_antigo}\n"
            "Para permanecer com o mesmo tipo clique ENTER\n\n"
            "[1] CORRIDA\n"
            "[2] FORÇA\n"
            "[3] SIMULADO HYROX\n\n"
            "Digite o tipo de treino: ")

        if (entrada == ""): #se estiver em branco é porque foi apertado ENTER e continua o antigo
            return ""

        try:
            tipo_treino = int(entrada)

            match tipo_treino:
                case 1:
                    return "CORRIDA"

                case 2:
                    return "FORÇA"

                case 3:
                    return "SIMULADO HYROX"

                case _:
                    clear()
                    print("Digite apenas 1, 2 ou 3!\n")
        except ValueError:
            clear()
            print("Resposta inválida!\n")