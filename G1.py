import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)


lista_noticias =[]

resposta = requests.get('https://g1.globo.com')

conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})



for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})

    #print(titulo.text)
    #print(titulo['href'])

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    if(subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text,'', titulo['href']])


news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)

print(news)




