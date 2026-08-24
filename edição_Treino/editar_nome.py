def editarOnome(nome_antigo):
    permanece = nome_antigo
    while True:
        nome_treino = input(f"\nPara permanecer com ({nome_antigo}) clique ENTER" 
                            "\n\nDigite o nome do treino: ").upper()

        if nome_treino == "": #se estiver em branco é porque foi apertado ENTER e continua o antigo
            return permanece
        else:
            return nome_treino