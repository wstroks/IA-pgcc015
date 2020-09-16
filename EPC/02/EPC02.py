# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 00:40:02 2020

@author: Washington Pagotto Batista
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


base_de_dados = pd.read_csv('dados.txt', header= None, sep=' ')
base_de_teste = pd.read_csv('teste.txt', header= None, sep=' ')

entrada_treinamento = base_de_dados.iloc[:,:5]
saida_treinamento = base_de_dados.iloc[:,5:]

x_treinamento = np.array(entrada_treinamento)
y_treinamento = np.array(saida_treinamento)

x_teste = np.array(base_de_teste)

taxa_de_aprendizagem = 0.0025
precisao = 10**-6

#função que retorna a classe do oléo
def funcao_classe(x):
    if(funcao_de_ativacao(x)!=1):
        return "Válvula A"
    else:
        return "Válvula B"
        
#função de ativação
def funcao_de_ativacao(u):
    if(u>=0):
        return 1
    else:
        return -1


#Inicializar o vetor de pesos com valores aleatórios;
def vetor_pesos_randomico():
    #como sabemos que a quantidade de entradas é 4
    return np.random.rand(5)

def criando_array(x):
    
    array=[]
    for l in range(x):
        array.append(0.)
    return array

#duvida do calculo testar (fiz pelo slide de matheus, fiquei na duvida se divide a cada somatorio ou depois)

def calculo_eqm(x,y,p):
    calculo_eqm=0
    resultado_final=0
    #padrao
    for a in range(35):
        sinal=criando_array(35)
        sinal[a]=somatorio(x, a, p)
        calculo_eqm = (calculo_eqm+math.pow((y[a]-sinal[a]),2))
    resultado_final= (calculo_eqm/35)
    return resultado_final

def somatorio(elemento,posicao, vetor):
    soma=0
    for j in range(5):
       soma+=elemento[posicao][j]*vetor[j]
        
    return soma
#slide de matheus
array_de_treinamento=[]
array_pesos=[]
#poderia fazer um array de array(melhorar codigo depois)
eqm_graf1=[]
eqm_graf2=[]
eqm_graf3=[]
eqm_graf4=[]
eqm_graf5=[]

def treinamento():
    contador=0
    while(contador!=5):
        EQM_ant=0
        EQM_atual=1
        epocas=0
        x=0
        vetor_inicial = vetor_pesos_randomico()
        x=0 + vetor_inicial
        array_pesos.append({'pesos_iniciais':x,"treinamento":contador+1})
        #print("pesos inicias", vetor_inicial)
                
        while(abs(EQM_atual-EQM_ant) > precisao):
            EQM_ant = EQM_atual;
            
            for i in range(35):
                u = criando_array(35);
                u[i]=somatorio(x_treinamento, i, vetor_inicial)
                for j in range(5):
                    calculo_taxa = taxa_de_aprendizagem*(y_treinamento[i] - u[i])
                    vetor_inicial[j] += calculo_taxa*x_treinamento[i][j];
              
            epocas = epocas + 1;
        
            EQM_atual = calculo_eqm(x_treinamento, y_treinamento, vetor_inicial)
            if(contador==0):
                eqm_graf1.append(EQM_atual)
            if(contador==1):
                eqm_graf2.append(EQM_atual)
            if(contador==2):
                eqm_graf3.append(EQM_atual)
            if(contador==3):
                eqm_graf4.append(EQM_atual)
            if(contador==4):
                eqm_graf5.append(EQM_atual)
        contador+=1
        array_de_treinamento.append({"epocas":epocas, "pesos_final":vetor_inicial,'treinamento': contador})
treinamento()
#print(array_pesos)   

arquivos = open('resultados.txt','w')
informacoes=""
for c in range(5):
    print(array_pesos[c])
    print(array_de_treinamento[c])
    informacoes+=str(array_pesos[c])+'\n'
    informacoes+=str(array_de_treinamento[c])+'\n'
    vetor = np.array(array_de_treinamento[c]['pesos_final'])
    y_teste = criando_array(15)
    for m in range(15):
        y_teste[m]=somatorio(x_teste, m, vetor)
        print(funcao_classe(y_teste[m]))
        informacoes+=str(funcao_classe(y_teste[m]))+'\n'
    print('----------------------------------------')
    informacoes+='----------------------------------------\n'
arquivos.write(informacoes)
arquivos.close()

#codigo ta sujo depois melhorar
def figuras(x,a):
    
    plt.figure(a)
    plt.title("Treinamento "+str(a))
    plt.xlabel('Quantidade de epocas')
    plt.ylabel('EQM')
    plt.plot(x)
    plt.savefig('treinamento'+str(a)+'.jpg')
    
figuras(eqm_graf1,1)    
figuras(eqm_graf2,2)  
figuras(eqm_graf3,3)  
figuras(eqm_graf4,4)  
figuras(eqm_graf5,5)  

plt.figure(6)
plt.title("Todas")
plt.xlabel('Quantidade de epocas')
plt.ylabel('EQM')
plt.plot(eqm_graf1)
plt.plot(eqm_graf2)
plt.plot(eqm_graf3)
plt.plot(eqm_graf4)
plt.plot(eqm_graf5)
plt.savefig('todas.jpg')


    
    
    