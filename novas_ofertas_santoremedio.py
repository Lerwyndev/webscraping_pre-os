import requests
from bs4 import BeautifulSoup



#USER AGENT
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}



#SELECIONAR PRODUTO
produto = input('Digite o produto: ')

produto = produto.replace(' ','%20')

#URL BASE

#url_bemol = "https://www.bemolfarma.com.br/listas/superoferta-farma" 
#url_mlivre = f'https://www.mercadolivre.com.br/{produto}'
url_ifood =f'https://www.ifood.com.br/busca?q={produto}'
#CONTAGEM

start = 1

# LOOP DE RASPAGEM

#while True:
url_final = url_ifood #+ str(start) + 'NoIndex_True'

    #FAZER A REQUISIÇÃO
r = requests.get(url_final,headers=headers)
site = BeautifulSoup(r.content,'html.parser')

# ENCONTRAR OS RESULTADOS
descricoes = site.find_all('h4', class_='merchant-list-carousel__item-title')
for i in descricoes:

    print(i.get_text())