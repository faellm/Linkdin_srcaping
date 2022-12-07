from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

#var do drive
#colocar o caminho do seu WebDriver driver = webdriver.Chrome('AQUIII')
driver = webdriver.Chrome('/Users/rafaellaramartins/Desktop/99freelas/Linkdin/chromedriver 2')

#email e senha

email = '' #seu email do Linkedin
password = '' #sua senha

#linkedin
url_link = 'https://www.linkedin.com/'


#id e class de componentes html

input_user = 'session_key' #id
input_pass = 'session_password' #id

btn_entrar = 'sign-in-form__submit-button' #class

btn_public = '//*[@id="ember77"]/div/div/div[1]/div[2]' #xpath

btn_pesquisar = 'search-global-typeahead__collapsed-search-button' #class
input_pesquisar = 'search-global-typeahead__input'

look_more_people = 'search-results__cluster-bottom-banner artdeco-button artdeco-button--tertiary artdeco-button--muted'
#################################################################



