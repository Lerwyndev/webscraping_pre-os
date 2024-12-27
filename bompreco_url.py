import requests
from bs4 import BeautifulSoup
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuração do arquivo de Google Sheets
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('Bom Precodrogaria').sheet1

# Função para extrair os dados da página
def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = []
    for product in soup.find_all('div', {'class': 'product'}):
        name = product.find('h2', {'class': 'product-name'}).text.strip()
        price = product.find('span', {'class': 'price'}).text.strip().replace('R$', '')
        products.append({'Name': name, 'Price': price})
    return products

# Função para criar o arquivo de Google Sheets
def create_sheet(products):
    df = pd.DataFrame(products)
    df.to_csv('bom_precodrogaria.csv', index=False)
    sheet.update_csv('bom_precodrogaria.csv')

# URL da página inicial do site
url = 'https://www.bomprecodrogaria.com.br/'

# Extrair os dados da página
products = extract_data(url)

# Criar o arquivo de Google Sheets
create_sheet(products)