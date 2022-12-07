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
    [sg.Text('Area de profissão: '), sg.Input()],
    [sg.Button('Pesquisar')]
]

#Janela
window = sg.Window('Linkedin Scraping', layout)

#Etapa 1.1 - ajustes do webdriver

#colocar o caminho do seu WebDriver driver = webdriver.Chrome('AQUIII')
driver = webdriver.Chrome('Linkdin_srcaping\chromedriver.exe')

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
    

#Ler os eventos do front end
while True:
    
    eventos, valores = window.read()
    #var do input do Layout
    input_profissional = (eventos, valores[0])  
    
    if eventos == sg.WINDOW_CLOSED:
        print('fechando...')
        break
        
    
    if eventos == 'Pesquisar':
        
        print('tudo correto.')
        Exec()
        
        
#fazer o scraping





