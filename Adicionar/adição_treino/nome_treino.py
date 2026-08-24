from funções_úteis.limpeza_terminal import clear
def nomeDOtreino(conteudo):
    while True:
        try:
            nomeTreino = input("Digite o nome do treino: ")
        except:
            if f"NOME DO TREINO: {nomeTreino.upper().strip()}" in conteudo: #UPPER deixa tudo em maiusculo e STRIP tira os espaços em branco
                print("O treino ja existe!\n")
                continue
        else:
            clear()
            break
    return nomeTreino