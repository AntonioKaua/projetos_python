from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())


driver = webdriver.Chrome(options=options, service=servico)

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

driver.get('https://www.youtube.com')



pesquisar = driver.find_element(By.TAG_NAME,'input')


pesquisar.send_keys('saiko')
pesquisar.submit()


video = driver.find_element(By.ID, "video-title")
video.click()



