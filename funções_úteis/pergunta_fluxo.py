from funções_úteis.limpeza_terminal import clear

def pergunta(): #a pergunta de continuação do sistema
    while True:
        resposta = input("Você quer continuar? s/n \nRESPOSTA: ").lower()
        #devolver valores booleanos para identificar a resposta
        if resposta == "s":
            clear()
            return True

        elif resposta == "n":
            return False
        else: 
            print("RESPOSTA INVÁLIDA!")