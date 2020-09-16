# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:48:25 2020

@author: Washington Pagotto Batista
"""

import pandas as pd
import numpy as np

base_de_dados = pd.read_csv('dados.txt', header= None, sep=' ')
base_de_teste = pd.read_csv('teste.txt', header= None, sep=' ')

entrada_treinamento = base_de_dados.iloc[:,:4]
saida_treinamento = base_de_dados.iloc[:,4:]

#Organizando dados de testes, adicionando um array de y_teste e transformando object em array

x_teste = np.array(base_de_teste)

#Transformando um objeto em um array
x_treinamento = np.array(entrada_treinamento)
y_treinamento= np.array(saida_treinamento)

#Inicializar taxa de aprendizagem
taxa_de_aprendizagem = 0.01

#função que retorna a classe do oléo
def funcao_classe(x):
    if(funcao_de_ativacao(x)!=1):
        return "Óleo C1"
    else:
        return "Óleo C2"
        
#função de ativação
def funcao_de_ativacao(u):
    if(u>=0):
        return 1
    else:
        return -1

#Inicializar o vetor de pesos com valores aleatórios;
def vetor_pesos_randomico():
    #como sabemos que a quantidade de entradas é 4
    return np.random.rand(4)
    
def criando_array(x):
    array=[]
    for l in range(x):
        array.append(0.)
    return array
        
        
#criando as saidas
y = criando_array((30));
y_teste= criando_array(10)
#seguindo o algoritmo do professor Matheus slide
array_de_treinamento=[]
array_de_pesos=[]
informacoes= ""

def somatorio(elemento,posicao, vetor):
    soma=0
    for j in range(4):
        soma+=elemento[posicao][j]*vetor[j]
    return soma
        
def treinamentos():
    #contador para quantidade de treinamentos que deseja fazer(OBS: como doc ta 5)
    contador=0
    
    while(contador!=5):
        #Inicializar o vetor de pesos com valores aleatórios;
        valor=0
        vetor_inicial = vetor_pesos_randomico()
        valor=valor+vetor_inicial
        array_de_pesos.append({"pesos_inicial":valor})
        print("Pesos inicias: ", vetor_inicial, " treinamento: ", contador+1)
        epocas=0
        condicao_error= True
        while(condicao_error):
            condicao_error=False
            for i in range(30):
                saida = criando_array((30));
                saida[i]=somatorio(x_treinamento, i, vetor_inicial)
                y[i] = funcao_de_ativacao(saida[i])
            
                if (y[i] != y_treinamento[i]):
                    for p in range(4):
                        taxa_atual= taxa_de_aprendizagem*(y_treinamento[i] - y[i])*x_treinamento[i][p]
                        vetor_inicial[p] = vetor_inicial[p] + taxa_atual;
                        condicao_error = True;
              
            epocas = epocas + 1;
            
                   
        contador+=1
        array_de_treinamento.append({"treinamento": contador,"epocas":epocas, "pesos_final":vetor_inicial})
    
   
treinamentos()


#Salvando dados em arquivo
arquivos = open('resultados.txt','w')


for c in range(5):
    print(array_de_treinamento[c])
    informacoes+=str(array_de_pesos[c])+'\n'
    informacoes+=str(array_de_treinamento[c])+'\n'
    vetor = np.array(array_de_treinamento[c]['pesos_final'])
    for b in range(10):
      y_teste[b]=somatorio(x_teste, b, vetor)
      print(funcao_classe(y_teste[b]))
      informacoes+=str(funcao_classe(y_teste[b]))+'\n'
    print('----------------------------------------')
    informacoes+='----------------------------------------\n'
arquivos.write(informacoes)
arquivos.close()
