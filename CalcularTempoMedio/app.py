# Instalar: pip install python-dateutil

from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcular_tempo_ativacao():
    # Solicitar ao usuário para inserir as datas
    data_ativacao = input("Insira a data de ativação (DD/MM/YYYY): ")
    data_desativacao = input("Insira a data de desativação (DD/MM/YYYY): ")
    
    # Converter strings de data para objetos datetime
    formato_data = "%d/%m/%Y"  # Definindo o formato das datas: DD/MM/YYYY
    try:
        data_ativacao_dt = datetime.strptime(data_ativacao, formato_data)
        data_desativacao_dt = datetime.strptime(data_desativacao, formato_data)
    except ValueError:
        print("Formato de data inválido. Insira as datas no formato DD/MM/YYYY.")
        return
    
    # Calcular a diferença entre as datas
    diferenca = relativedelta(data_desativacao_dt, data_ativacao_dt)
    
    # Retornar a diferença em anos, meses e dias
    print(f"O cliente ficou ativo por {diferenca.years} anos, {diferenca.months} meses e {diferenca.days} dias.")

# Executar o programa
calcular_tempo_ativacao()