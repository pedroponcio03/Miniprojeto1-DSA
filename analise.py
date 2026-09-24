#Limpeza de dados e análise
import pandas as pd
import numpy as np
import tabela
import matplotlib.pyplot as plt
def analise_dados(df):
    df['Status_Entrega'] = df['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')
    top_10_produtos = df.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending = False).head(10)
    #Multiplica preco unitario e quantidade e retorna como valor de faturamento
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'])
    df['Faturamento'] = df['Preco_Unitario'] * df['Quantidade']
    df['Mes'] = df['Data_Pedido'].dt.to_period('M')
    #Transformando data para datetime do pandas, agrupando por mês, soma e faturamento
    faturamento_mensal = df.groupby('Mes')['Faturamento'].sum() #agrupa por mês, somando o faturamento
    faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m') #Transformando em string
    faturamento_mensal.map('R$ {:,.2f}'.format)

    #Utilizando o matplotlib
    # Cria uma nova figura com tamanho de 12 por 6 polegadas
    plt.figure(figsize=(12, 6))

    # Plota os dados de faturamento mensal em formato de linha
    faturamento_mensal.plot(kind='line', marker='o', linestyle='-', color='green')

    # Define o título do gráfico com fonte de tamanho 16
    plt.title('Evolução do Faturamento Mensal', fontsize=16)

    # Define o rótulo do eixo X
    plt.xlabel('Mês', fontsize=12)

    # Define o rótulo do eixo Y
    plt.ylabel('Faturamento (R$)', fontsize=12)

    # Rotaciona os valores do eixo X em 45 graus para melhor visualização
    plt.xticks(rotation=45)

    # Adiciona uma grade com estilo tracejado e linhas finas
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Ajusta automaticamente os elementos para evitar sobreposição
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()

    return(df)