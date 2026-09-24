# Instala o pacote watermark
import os
os.system("pip install -q -U watermark")
# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd  

# Importação da biblioteca NumPy para operações matemáticas e arrays
import numpy as np  

# Importação da biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt  

# Importação da biblioteca Seaborn para visualização estatística de dados
import seaborn as sns  

# Importação da biblioteca random para geração de números aleatórios
import random  

# Importação das classes datetime e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta  

"""

Versões dos pacotes
matplotlib: 3.10.0
numpy     : 2.1.3
pandas    : 2.3.1
seaborn   : 0.13.2

"""

import tabela
import analise

if __name__ == "__main__":

    '''Gera uma tabela fictícia caso eu precise utilizar em uma tabela real,
     somente vou substituir o valor de df com o pd.(read.csv)'''

    df = tabela.gerar_dados_ficticios()
    #Limpa os dados
    df = analise.analise_dados(df)
    print(df.head(50))
