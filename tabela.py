#Importação
import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# Definição de função para geração de dados fictícios de vendas
def gerar_dados_ficticios(num_registros = 600):
    #Mensagem inicial
    print(f"\n Iniciando a geração de {num_registros} numeros de vendas...");

    # Dicionário com produtos, suas categorias e preços
    produtos = {
    'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500},
    'Mouse vertical': {'categoria': 'Acessorios', 'preco': 250},
    'Teclado Mecânico': {'categoria': 'Acessorios', 'preco': 550},
    'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800},
    'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200},
    'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800},
    'Placa de vídeo': {'categoria': 'Hardware', 'preco': 4500},
    'SSD 1TB': {'categoria': 'Hardware', 'preco': 600},
    }

    # Cria uma lista apenas com os nomes dos produtos

    lista_produtos = list(produtos.keys());

    # Dicionário com nome das cidades e seus respectivos Estados
    cidades_estados = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Belo Horizonte': 'MG',
    'Porto Alegre': 'RS',
    'Salvador': 'BA',
    'Curitiba': 'PR',
    'Fortaleza': 'CE',
    }

    # Cria uma lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estados.keys())

    # Lista que armazena os registros de vendas
    dados_vendas = []

    # Define a data inicial dos pedidos
    data_inicial = datetime(2026, 1, 1)

    # Loop para gerar registro de vendas
    for i in range(num_registros):

        # Seleciona aleatoriamente o produtos
        produto_nome = random.choice(lista_produtos)

        # Seleciona aleatoriamente uma cidade
            
        cidade = random.choice(lista_cidades)

        # Gera uma quantidade de produtos vendidas entre 1 a 7
        quantidade = np.random.randint(1, 8)

        # Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        # Se o produto for Mouse ou Teclado, aplica desconto, aleatório de ate 10%
        if produto_nome in ['Mouse vertical', 'Teclado Mecânico']:
                preco_unitario = produtos[produto_nome] ['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome] ['preco'];

        # Adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })

    # Mensagem final indicando que a geração terminou
    print("Geração de dados concluída. \n")

    # Retorna os dados no formato de DataFrame
    return pd.DataFrame(dados_vendas)
#Executa
def executar():
    print("Executando o miniprojeto...")
    df = gerar_dados_ficticios()
    print(df.head())  # Exibe as primeiras linhas do DataFrame no terminal


if __name__ == "__main__":
    executar()