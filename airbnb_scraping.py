from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import openpyxl


dados_hospedagens = []

hospedagens = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('window-size=800,1600')
servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=servico)
driver.get('https://www.airbnb.com.br/')
sleep(1)


fechar = driver.find_element(By.TAG_NAME, "button")
ac = ActionChains(driver)
ac.move_to_element(fechar).move_by_offset(250, 0).click().perform()

sleep(1)



local = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div[1]/div[1]/label/div/input")
local.send_keys("São Paulo")
sleep(2)
local.submit()

sleep(2)
page_content = driver.page_source
site = BeautifulSoup(page_content, 'html.parser')

hospedagens = site.findAll('div', attrs={'itemprop': 'itemListElement'})

for hospedagem in hospedagens:

    hospedagem_nome = hospedagem.find('div', attrs={'data-testid': 'listing-card-title'}).text
    hospedagem_descricao = hospedagem.find('span', attrs={"data-testid": "listing-card-name"}).text
    hospedagem_url = hospedagem.find('meta', attrs={"itemprop": "url"})
    preco = hospedagem.find('span', attrs={'class': 'a8jt5op atm_3f_idpfg4 atm_7h_hxbz6r atm_7i_ysn8ba atm_e2_t94yts atm_ks_zryt35 atm_l8_idpfg4 atm_mk_stnw88 atm_vv_1q9ccgz atm_vy_t94yts dir dir-ltr'}).text
    hospedagem_url = hospedagem_url['content']
    dados_hospedagens.append([hospedagem_nome, hospedagem_url, hospedagem_descricao, preco])


dados = pd.DataFrame(dados_hospedagens, columns=['Nome', 'URL', 'Descrição', 'Preço'])

dados.to_excel('hospedagens.xlsx', index=False)
