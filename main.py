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

from edição_Treino.editar_nome import editarOnome
from edição_Treino.editar_tipo import editarOtipo
from edição_Treino.editar_intensidade import editarAintensidade

open("Sistema de Treinos.txt", "a").close()

clear()
while True:
   print("==========BEM VINDO AO HYROX PLANNER=========")
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

    case 5:
        conteudo = abrir_leitura()
        treinos = conteudo.split("\n\n")
        treino_encontrado = None

        treino_antigo = input("Digite qual treino deseja editar: ").upper().strip()

        for treino in treinos:
            if f"NOME DO TREINO: {treino_antigo}\n" in treino:
                treino_encontrado = treino
                break

        if treino_encontrado is None:
            print("Treino inexistente!")
            continue


        linhas = treino_encontrado.split("\n")

        
        nome_antigo = linhas[0].replace("NOME DO TREINO: ", "")
        tipo_antigo = linhas[1].replace("TIPO DE TREINO: ", "")
        data_antiga = linhas[2].replace("DATA DO TREINO: ", "")
        duracao_antiga = linhas[3].replace("DURAÇÃO DO TREINO: ", "")
        intensidade_antiga = linhas[4].replace("INTENSIDADE DO TREINO: ", "")

        clear()
        novo_nome = editarOnome(nome_antigo)
        if novo_nome == "":
            novo_nome = nome_antigo
        
        clear()
        novo_tipo = editarOtipo(tipo_antigo)
        if novo_tipo == "":
            novo_tipo = tipo_antigo

        clear()
        from datetime import datetime
        while True:
            nova_data = input(f"Data atual: {data_antiga}\n"
                               "Nova data (DD/MM/AAAA) (ENTER para manter): ").strip()
            if nova_data == "":
                nova_data = data_antiga
                break
            try:
                datetime.strptime(nova_data, "%d/%m/%Y") #so permite datas válidas e existentes
                break
            except ValueError:
                clear()
                print("Data inválida! Use o formato DD/MM/AAAA.\n")


        clear()
        nova_duracao = input(
            f"Duração atual: {duracao_antiga}\nDigite ENTER para manter\n"
            "Nova duração: ").strip()

         # se apertar ENTER continua o mesmo
        if nova_duracao == "":
            nova_duracao = duracao_antiga

        clear()
        nova_intensidade = editarAintensidade(intensidade_antiga)
        if nova_intensidade == "":
            nova_intensidade = intensidade_antiga


        dados_novos = (
            "Dados do Treino:"
            "\nNOME DO TREINO: " + novo_nome.upper()
            + "\nTIPO DE TREINO: " + novo_tipo
            + "\nDATA DO TREINO: " + nova_data
            + "\nDURAÇÃO DO TREINO: " + nova_duracao
            + "\nINTENSIDADE DO TREINO: " + nova_intensidade)

        for i in range(len(treinos)):
            if f"NOME DO TREINO: {treino_antigo}" in treinos[i]:
                treinos[i] = dados_novos

        novo_conteudo = "\n\n".join(treinos)

        with open("Sistema de Treinos.txt", "w") as treino:
            treino.write(novo_conteudo)

        clear()
        print("Treino editado com sucesso!")

    case 6:
        conteudo = abrir_leitura()
        divisor = "----------------------------------------"
        blocos = conteudo.split(divisor)
        
        treinos = [t.strip() for t in blocos if t.strip()]
        
        while True: 
            treino_excluir = input("Digite o treino que deseja excluir: ").strip().upper()
            existe = any(f"NOME DO TREINO: {treino_excluir}" in t.upper() for t in treinos)
            
            if not existe:
                clear()
                print("Treino inexistente!\n")
                continue
            else:
                clear()
                break
    
        tag_busca = f"NOME DO TREINO: {treino_excluir}"
        conjunto_fica = [t for t in treinos if tag_busca not in t.upper()]
    
        if conjunto_fica:
            conteudo_atualizado = "\n\n".join(conjunto_fica) + f"\n{divisor}\n"
        else:
            conteudo_atualizado = ""

        with open("Sistema de Treinos.txt", "w", encoding="utf-8") as file:
            file.write(conteudo_atualizado)
        
        print("Treino Excluído Com Sucesso!\n\n")