def abrir_leitura():
    treino = open("Sistema de Treinos.txt", "r")
    conteudo = treino.read()
    treino.close()

    return conteudo