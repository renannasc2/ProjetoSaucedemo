import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import time

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
site = os.getenv('SITE')
loginSucess = os.getenv('LOGIN_SUCESS')
passUser = os.getenv('PASSWORD')


def login(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    print("Acessei o site ✔")
    page.goto(site)

    print("Preenchi o usuario ✔")
    page.fill('[data-test="username"]', loginSucess)

    time.sleep(1)

    print("Preenchi a senha ✔")
    page.fill('[data-test="password"]', passUser)

    print("Cliquei no botão Logar ✔")
    page.click('[data-test="login-button"]')

    time.sleep(3)

    browser.close()

def openAbout(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    print("Acessei o site ✔")
    page.goto(site)
    print("Preenchi o usuario ✔")
    page.fill('[data-test="username"]', loginSucess)
    print("Preenchi a senha ✔")
    page.fill('[data-test="password"]', passUser)
    print("Cliquei no botão Logar ✔")
    page.click('[data-test="login-button"]')


    print('Cliquei em "Sobre" ✔')
    page.click('[id="react-burger-menu-btn"]')

    time.sleep(2)

    page.click('[id="react-burger-cross-btn"]')

    time.sleep(3)
    browser.close()

def addItens(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    print("Acessei o site ✔")
    page.goto(site)
    print("Preenchi o usuario ✔")
    page.fill('[data-test="username"]', loginSucess)
    print("Preenchi a senha ✔")
    page.fill('[data-test="password"]', passUser)
    print("Cliquei no botão Logar ✔")
    page.click('[data-test="login-button"]')


    print('Cliquei para abrir o "Menu lateral" ✔')
    page.click('[id="react-burger-menu-btn"]')
    print('Cliquei para fechar o "Menu lateral" ✔')
    page.click('[id="react-burger-cross-btn"]')

    print('Adicionei a bolsa ao carrinho ✔')
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    print('Adicionei a bicicleta ao carrinho ✔')
    page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')

    print('Cliquei no carrinho ✔')
    page.click('[data-test="shopping-cart-link"]')

    print('Cliquei em checkout ✔')
    page.click('[data-test="checkout"]')

    time.sleep(2)
    #Preenche as info de checkout
    print('Estou preenchendo as infos ...')
    page.fill('[data-test="firstName"]', 'Cleitin')
    page.fill('[data-test="lastName"]', 'Rei delas!')
    page.fill('[data-test="postalCode"]','7070-70dnv')
    print('Nome, ultimo nome e cep preenchidos ✔')
    time.sleep(2)
    page.click('[data-test="continue"]')
    print('Cliquei em Continuar ✔')

    time.sleep(5)

    page.click('[data-test="finish"]')
    print('Cliquei em Finish ✔')

    time.sleep(5)

    browser.close()


with sync_playwright() as playwright:
    login(playwright)
    openAbout(playwright)
    addItens(playwright)
