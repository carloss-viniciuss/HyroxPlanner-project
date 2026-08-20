from limpeza_terminal import clear

def validar_data():
    from datetime import datetime
    while True:
        try:
            data = input("Digite a data do treino (dd/mm/aaaa): ")
            data_formatada = datetime.strptime(data, "%d/%m/%Y") #para que so aceite o formato de data

            clear()
            return data
                
        except ValueError:
            clear()
            print("Data inválida! Use o formato dd/mm/aaaa.\n")
            continue