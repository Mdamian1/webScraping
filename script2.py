# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup
#from django.shortcuts import render

page = requests.get("http://localhost/topicosavancados/Trabalho/pega.php")
soup = BeautifulSoup(page.content, 'html.parser')
soup
    
tabelas = soup.select(".table")
arrayPontos = {}
arrayCabecalhos = []
arrayValores = []
ponto = []
coletas = []

n = len(tabelas)
for i in range(1, n, 2):
    cabecalhos = soup.select(".table")[i]
    for k in range(0,4,1):
        cabChave = cabecalhos.select("label b")[k].get_text()
        cabChave = cabChave.replace(":", "")
        
        cabValor = cabecalhos.select("label")[k].get_text()
        cabValor = cabValor.replace(cabChave+": ", "")
        
        cabChave = cabChave.replace(" ", "_")

        arrayCabecalho = ({
            cabChave : cabValor
        })
        ponto.append(arrayCabecalho)  
    arrayPontos.update({
        i : {
            'descricao' : ponto,
        }
    })
    ponto = []

    

for j in range(2, n+1, 2):
    
    Datas = []
    Horas = []
    Ventos = []
    Mares = []
    Chuvas = []
    Aguas = []
    Ares = []
    Ecolis = []
    Condicoes = []
    valores = soup.select(".table")[j]
    for l in range(0,n-1,1):
        datas = valores.select(".data")[l].get_text()
        horas = valores.select(".hora")[l].get_text()
        ventos = valores.select(".vento")[l].get_text()
        mares = valores.select(".mare")[l].get_text()
        chuvas = valores.select(".chuva")[l].get_text()
        aguas = valores.select(".agua")[l].get_text()
        ares = valores.select(".ar")[l].get_text()
        ecolis = valores.select(".ecoli")[l].get_text()
        condicoes = valores.select(".condicao")[l].get_text()
        
        Datas.append(datas)
        Horas.append(horas)
        Ventos.append(ventos)
        Mares.append(mares)
        Chuvas.append(chuvas)
        Aguas.append(aguas)
        Ares.append(ares)
        Ecolis.append(ecolis)
        Condicoes.append(condicoes)
        
        arrayColetas = ({
            "data" : Datas[l],
            "hora" : Horas[l],
            "vento" : Ventos[l],
            "mare" : Mares[l],
            "chuva" : Chuvas[l],
            "agua" : Aguas[l],
            "ar" : Ares[l],
            "ecolis" : Ecolis[l],
            "condicao" : Condicoes[l]
        })
        
        coletas.append(arrayColetas)

    arrayPontos[j-1].update({
        
        'coletas' : coletas,
        
    })
    coletas = []
#print(arrayPontos)
with open('meu_arquivo.json', 'w') as f:
    json.dump(arrayPontos, f)