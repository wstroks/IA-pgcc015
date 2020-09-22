# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:20:29 2020

@author: Washington Pagotto Batista
"""

import pandas as pd
import numpy as np
import math

base_de_treinamento = pd.read_csv('dataset/iris/txt/iris-10-1tra.txt', sep=',')
base_de_test = pd.read_csv('dataset/iris/txt/iris-10-1tst.txt', sep=',')

x_treinamento = base_de_treinamento.iloc[:,:4]
y_treinamento = base_de_treinamento.iloc[:,4:]

x_teste = base_de_test.iloc[:,:4]
y_teste= base_de_test.iloc[:,4:]

taxa_de_aprendizado = 0.1
precisao = 10**-6
beta = 0.5
a= y_teste.size
def funcao_conversao_matrix_saida(matrix,saidas_possiveis):
    # Iris-setosa, Iris-versicolor, Iris-virginica
    vetor = np.array(matrix)
    print(vetor)
    auxiliar_matrix = np.zeros((matrix.size,saidas_possiveis))
    print(auxiliar_matrix)
    for i in range(matrix.size):
        if vetor[i][0]==' Iris-setosa':
            auxiliar_matrix[i][0]=1
            auxiliar_matrix[i][1]=0
            auxiliar_matrix[i][2]=0        
        elif vetor[i][0]==' Iris-versicolor':
            auxiliar_matrix[i][0]=0
            auxiliar_matrix[i][1]=1
            auxiliar_matrix[i][2]=0 
        elif vetor[i][0]==' Iris-virginica':
            auxiliar_matrix[i][0]=0
            auxiliar_matrix[i][1]=0
            auxiliar_matrix[i][2]=1 
    return auxiliar_matrix

def funcao_sigmoid(u, b):
    calculo =(1/(1+(math.exp(-u*b))))
    return calculo


def funcao_derivada_sigmoid(u,b):
    calculo = b*funcao_sigmoid(u, b)*(1-(funcao_sigmoid(u, b)))
    return calculo

def criando_matriz(linhas, colunas):
    randomico = randomizando_matriz(np.zeros((linhas,colunas), dtype=np.float64), linhas,colunas)
    return randomico

def criando_array(qtd):
    return np.zeros((qtd), dtype=np.float64)

def randomizando_matriz(matriz, linha, coluna):
    y=0;
    x=0;
    x=linha-1;
    y=coluna-1;
    for i in range(linha):
        for j in range(coluna):
            matriz_rand=np.random.random(1) 
            matriz[i][j]=matriz_rand  
    return matriz;

#https://www.youtube.com/watch?v=FSvD2HT0Zfg&ab_channel=ML4U explicação
def criando_camada_escondida(entrada,camada_escondida):
    #vale ressaltar que a matrix da camada escondida é numero de hiden e a coluna é o numero de entradas +1 que corresponde ao teta
    return criando_matriz(camada_escondida, entrada+1)

def criando_camada_saida(camada_escondida, saida):
    return criando_matriz(saida, camada_escondida+1)

camada_escondida = criando_camada_escondida(x_treinamento.columns.size, x_treinamento.columns.size)
camada_saida = criando_camada_saida(x_treinamento.columns.size,y_treinamento.columns.size*3)    

y_treinamento_numerico=funcao_conversao_matrix_saida(y_treinamento,3)
y_teste_numerico=funcao_conversao_matrix_saida(y_teste,3)