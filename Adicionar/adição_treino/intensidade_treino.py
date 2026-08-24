from funções_úteis.limpeza_terminal import clear

def intensidadeDEtreino():
    while True:
        try:
            intensidade_treino = int(input("[1] - LEVE / [2] - MODERADO / [3] - PESADO"
                                            "\nDigite o número de intensidade: "))

            match intensidade_treino:
                case 1:
                    intensidade_final = "Treino Leve"

                case 2:
                    intensidade_final = "Treino Moderado"

                case 3:
                    intensidade_final = "Treino Pesado"

        except:
            clear()
            print("Resposta Inválida!")
            continue
        
        else:
            break
    clear()
    return intensidade_final