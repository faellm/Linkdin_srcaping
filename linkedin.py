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

#criar options

from PySimpleGUI import PySimpleGUI as sg

#Layout
#DarkBlue19
sg.theme('Reddit')
layout = [
    [sg.Text('Area de profissão: '), sg.Input()],
    [sg.Button('Pesquisar')]
]

input_profissional = 'Engenheiro de software'

#Janela
janela = sg.Window('Linkedin Scraping', layout)

#var do drive
#colocar o caminho do seu WebDriver driver = webdriver.Chrome('AQUIII')
driver = webdriver.Chrome('Linkdin_srcaping\chromedriver.exe')


sleep(3)

print('> Entrou no Chrome ! <')

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

    #pesquisar profissional
    """ btn_search = driver.find_element(By.CLASS_NAME, input_pesquisar)
    btn_search.send_keys(input_profissional)
    btn_search.send_keys(Keys.ENTER) """
            
    sleep(1.5)
            
    #url das pessoas
    url_people = f'https://www.linkedin.com/search/results/people/?keywords={input_profissional}'

    driver.get(url_people) 

#Ler os eventos do front end
while True:
    
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        
        break
    
    if eventos == 'Pesquisar':
        
        Exec()





