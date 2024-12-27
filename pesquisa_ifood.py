import requests
from bs4 import BeautifulSoup

# USER AGENT
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# SELECIONAR PRODUTO
produto = input('Digite o produto: ')
produto = produto.replace(' ', '%20')

# URL BASE
url_ifood = f'https://www.ifood.com.br/busca?q={produto}'

# FAZER A REQUISIÇÃO
r = requests.get(url_ifood, headers=headers)

# Verificar se a requisição foi bem-sucedida
if r.status_code == 200:
    # Parsear o HTML retornado
    site = BeautifulSoup(r.content, 'html.parser')

    # Verificar o HTML para ajustar os seletores
    print(site.prettify())  # Mostra o HTML retornado para ajudar no debug

    # Tentativa de encontrar as descrições
    descricoes = site.find_all('h4', class_='merchant-list-carousel__item-title')
    if descricoes:
        for i in descricoes:
            print(i.get_text())
    else:
        print("Nenhum elemento encontrado. Verifique o HTML retornado e ajuste o seletor.")
else:
    print(f"Erro na requisição. Código de status: {r.status_code}")
