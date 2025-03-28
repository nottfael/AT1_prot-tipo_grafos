import sys
import numpy as np

#  Carrega a matriz de um arquivo .txt
def carregar_matriz(dataset):
    caminho = './grafos_datasets/' + dataset + '.txt' # Montando o caminho para chegar ao arquivo
    matriz = np.loadtxt(caminho, dtype='int32') # Lê o arquivo como uma matriz de inteiros
    return matriz

def salvar_resultado(dataset, linhas, colunas):
    """
    Salva as informações da matriz em "resultados.txt".
    - Cada novo resultado é adicionado no final do arquivo.
    """
    with open('resultados.txt', 'a') as arquivo:
        arquivo.write(f'{dataset}.txt = {linhas} linhas e {colunas} colunas\n')

# Função 3: Retorna as dimensões da matriz (linhas, colunas)
def dimensao_matriz(matriz):
    return matriz.shape


if __name__ == '__main__':
    """
    Pede o nome do arquivo ao usuário
    Carrega a matriz do arquivo
    Obtém as dimensões da matriz
    Salva e exibe o resultado
    """
    arquivo = input('Nome do dataset: ')
    matriz = carregar_matriz(arquivo)
    linhas, colunas = dimensao_matriz(matriz)
    salvar_resultado(arquivo, linhas, colunas)
    print(f"Matriz '{arquivo}' carregada com sucesso!")
    print(f"Linhas: {linhas}, Colunas: {colunas}")


