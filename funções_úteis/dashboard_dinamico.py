def dashboard():

    try:
        arquivo = open("Sistema de Treinos.txt", "r")
        conteudo = arquivo.read()
        arquivo.close()

        total_treinos = conteudo.count("NOME DO TREINO:") #quantidade de treinos

    except FileNotFoundError:
        total_treinos = 0

    try:
        comp = open("Competições.txt", "r")
        conteudo_comp = comp.read()
        comp.close()

        total_comp = conteudo_comp.count("==========") #quantidade de competicoes

    except FileNotFoundError:
        total_comp = 0

    print("\t==========DASHBOARD==========\n")
    print(f"\tTreinos cadastrados: {total_treinos}")
    print(f"\tCompetições cadastradas: {total_comp}\n")