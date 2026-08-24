from funções_úteis.limpeza_terminal import clear
from funções_úteis.dashboard_dinamico import dashboard
from funções_úteis.leitura import abrir_leitura
from funções_úteis.validação_data import validar_data
from funções_úteis.calculo_dias import dias_restantes
from funções_úteis.pergunta_fluxo import pergunta

from Adicionar.adição_treino.nome_treino import nomeDOtreino
from Adicionar.adição_treino.intensidade_treino import intensidadeDEtreino
from Adicionar.adição_treino.tipo_treino import tipoDEtreino

from Adicionar.competicao.add_competicao import adicionar_competicao

open("Sistema de Treinos.txt", "a").close()

clear()
while True:
   print("==========BEM VINDO AO HYROX PLANNER=========dicionar")
   dashboard()
   opcao_escolhida = int(input("Você deseja:" 
    "\n[1] Adicionar Treino\n"
        "[2] Adicionar competição\n"
        "[3] Visualizar treinos \n"
        "[4] Visualizar competições\n"
        "[5] Editar\n"
        "[6] Excluir\n"
        "[7] Controle de Desempenho\n"
        "[8] Acompanhar Evolução\n"
        "[9] Sugestões Personalizadas\n"
        "[11] Parar"
        "\nRESPOSTA: "))
   clear()

   match opcao_escolhida:
    case 1:
        conteudo = abrir_leitura()
        nomeTreino = nomeDOtreino(conteudo)
        clear()
        tipo = tipoDEtreino()
        clear()
        intensidade_final = intensidadeDEtreino()
        data_treino = validar_data()
        duracao_treino = input("Digite o tempo de duração: ")

        dados_novos = (
            f"NOME DO TREINO: {nomeTreino.upper().strip()}\n"
            f"TIPO DE TREINO: {tipo}\n"
            f"DATA DO TREINO: {data_treino}\n"
            f"DURAÇÃO DO TREINO: {duracao_treino}\n"
            f"INTENSIDADE DO TREINO: {intensidade_final}\n"
            f"----------------------------------------\n"
        )

        with open("Sistema de Treinos.txt", "a", encoding="utf-8") as file:
            file.write(dados_novos)

        clear()
        print("Treino Adicionado com Sucesso!\n")

    case 2:
        import datetime
        name_comp = input("Digite o nome da competição:")
        while True:
            date_comp = input("Digite a data da competição (DD/MM/AAAA): ")
            try:
                datetime.datetime.strptime(date_comp.strip(), "%d/%m/%Y").date()
                break

            except ValueError:
                print("Data inválida ou fora do padrão (DD/MM/AAAA). Tente novamente!\n")

        local_comp = input("Digite o local da competição:")
        cat_comp = input("Digite a categoria da competição:")

        adicionar_competicao(name_comp,date_comp,local_comp,cat_comp)
        clear()
        print("Competição adicionada com sucesso!\n\n")
        pergunta()

    case 3:
        clear()
        treino = abrir_leitura()
        print(treino)
        if not pergunta():
            break

    case 4:
        print("==========COMPETIÇÕES==========")
        try:
            with open("Competições.txt","r") as file_competition:
                file_comp = file_competition.read()

            if file_comp.strip() == "":
                print("Nenhuma competição cadastrada")
            else:
                print(file_comp)

        except FileNotFoundError:
            print("Nenhuma competição cadastrada ainda.")
                  
        if not pergunta():
            break