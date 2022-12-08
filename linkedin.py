from dados import url_link
from dados import email
from dados import password
from dados import *
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from PySimpleGUI import PySimpleGUI as sg

#Etapa 1.0 - criando o Layout em SimpleGui
sg.theme('Reddit')
layout = [
    [sg.Text('Pesquisa ')],
    [sg.Input()],
    [sg.Text('1 pagina = 10 pessoas')],
    [sg.Text('Quantas você deseja capturar? ')],
    [ sg.Input()],
    [sg.Button('Pesquisar')]
]


#Janela
window = sg.Window('Linkedin Scraping', layout)

#Etapa 1.1 - ajustes do webdriver

#colocar o caminho do seu WebDriver driver = webdriver.Chrome('AQUIII')
driver = webdriver.Chrome('/Users/rafaellaramartins/Desktop/99freelas/chromedriver - cópia')

sleep(3)

def Exec():
    
    primaria = driver.get(url_link)
    primaria
    
    #logando no Linkedin
    entrar = driver.find_element(By.ID, input_user)
    entrar.send_keys(email)

    sleep(3)

    senha = driver.find_element(By.ID, input_pass)
    senha.send_keys(password)

    buttun_entrar= driver. find_element(By.CLASS_NAME, btn_entrar)
    sleep(1)
    buttun_entrar.click()
    sleep(5)
            
    #url dos profissionais
    url_people = f'https://www.linkedin.com/search/results/people/?keywords={input_profissional}'
    #abrindo direto a pagina
    driver.get(url_people)
    
    
    
    
    def scraping():

            #### fazer scraping de perfil ######
            def GetURL():
                page_source = BeautifulSoup(driver.page_source)
                profiles = page_source.find_all('a', class_ = 'app-aware-link')
                #('a', class_ = 'search-result__result-link ember-view')
                all_profile_URL = []
                for profile in profiles:
                    profile_ID = profile.get('href')
                    profile_URL = "https://www.linkedin.com" + profile_ID
                    #profile_URL = profile.get('href')
                    if profile_URL not in all_profile_URL:
                        
                        all_profile_URL.append(profile_URL)
                        
                        print(all_profile_URL)
                        
                return all_profile_URL
            GetURL()
    scraping()
    
#Ler os eventos do front end
while True:
    
    eventos, valores = window.read()
    #var do input do Layout
    #input_profissional = (eventos, valores[1])
    #input_page = (eventos, valores[2])  
    
    input_profissional = input('pesquisar: ')
    
    if eventos == sg.WINDOW_CLOSED:
        
        print('fechando...')
        break
        
    
    if eventos == 'Pesquisar':
        
        print('tudo correto.')
        Exec()
        break
        






