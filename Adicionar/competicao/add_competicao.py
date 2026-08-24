from funções_úteis.calculo_dias import dias_restantes

def adicionar_competicao(name_comp,date_comp,local_comp,cat_comp):

    status_dias = dias_restantes(date_comp) 
    
    dados_competicao =(f"\n=========={name_comp}==========\n"
                       f"DATA: {date_comp} \t{status_dias}\n"
                       f"LOCAL: {local_comp}\n"
                       f"CATEGORIA: {cat_comp}\n")

    with open("Competições.txt","a") as file:
        file.write(dados_competicao)