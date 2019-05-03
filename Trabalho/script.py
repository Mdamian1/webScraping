# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

page = requests.get("http://localhost/topicosavancados/Trabalho/pega.php")
soup = BeautifulSoup(page.content, 'html.parser')
soup

tabelas = soup.select(".table")

n = len(tabelas)
for i in range(1, n, 2):
    cabecalhos = soup.select(".table")[i].get_text()
    print(cabecalhos)
    
for j in range(2, n+1, 2):
    valores = soup.select(".table")[j].get_text()
    print(valores)
