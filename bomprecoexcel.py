from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

# Configuração do Selenium
service = Service('C:\\Users\\frank.valladares\\Desktop\\PROJETO WEBSCRAPING\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Acessar o site
url = 'https://www.bomprecodrogaria.com.br/'
driver.get(url)

# Esperar o carregamento da página
driver.implicitly_wait(10)

# Extração com BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
products = []
for product in soup.find_all('div', {'class': 'product'}):  # Ajuste conforme o HTML real
    try:
        name = product.find('h2', {'class': 'product-name'}).text.strip()
        price = product.find('span', {'class': 'price'}).text.strip().replace('R$', '')
        description = product.find('p', {'class': 'product-description'}).text.strip()  # Ajuste conforme necessário
        department = product.find('div', {'class': 'product-department'}).text.strip()  # Ajuste conforme necessário
        products.append({'Name': name, 'Price': price, 'Description': description, 'Department': department})
    except AttributeError:
        continue

# Salvar os dados no Excel
df = pd.DataFrame(products)
df.to_excel('bom_precodrogaria.xlsx', index=False)

# Fechar o navegador
driver.quit()
