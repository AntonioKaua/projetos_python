import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

url_base = 'https://lista.mercadolivre.com.br/'

produto_input = input('O que você deseja?')

response = requests.get(url_base + produto_input)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class':['andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16', 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated']})


for produto in produtos:
    nome = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})

    price = produto.find('span', attrs={'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'})

    lista_produtos.append([nome.text, price.text, link['href']])

Resultado = pd.DataFrame(lista_produtos, columns=['Nome', 'Preço', 'Link'])
Resultado.to_excel(f'Resultado_de_pesquisa_{produto_input}.xlsx', index=False)

print(Resultado)