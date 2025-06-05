import pandas as pd
def carrega(caminho):
    dados = pd.read_csv("PythonProjects/dados", sep=';')
    dados = dados.sort_values(by=['Data'])
    del dados['Data']
    return dados
