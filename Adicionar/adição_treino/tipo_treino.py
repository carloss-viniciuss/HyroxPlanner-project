from funções_úteis.limpeza_terminal import clear

def tipoDEtreino():
    while True:
        try:
            tipo_treino = int(input("[1] CORRIDA / [2] FORÇA / [3] SIMULADO HYROX " \
                                    "\n\nDigite o tipo de treino entre os disponíveis: " ))
            
            match tipo_treino:
                case 1:
                    tipo = "CORRIDA"
                
                case 2:
                    tipo = "FORÇA"
            
                case 3:
                    tipo = "SIMULADO HYROX"
            
        except (ValueError, TypeError): 
            clear()
            print("Resposta inválida!")
            continue
        else:
            break
    clear()
    return tipo
