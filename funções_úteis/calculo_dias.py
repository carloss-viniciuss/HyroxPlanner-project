def dias_restantes(data_):
    import datetime
    try:
        data_evento = datetime.datetime.strptime(data_.strip(), "%d/%m/%Y").date() #o .date tira o horario e so deixa a data
        data_hoje = datetime.date.today() #data atual do computador
        diferenca = data_evento - data_hoje #pra saber quantos dias faltam
        
        if diferenca.days > 0:
            return f"Faltam {diferenca.days} dias"
        elif diferenca.days == 0: #hojeee
            return "É HOJE!"
        else:
            return f"Aconteceu há {abs(diferenca.days)} dias" #abs tira o negativo! pois é passado
    except ValueError:
        return "Data inválida"