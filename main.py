import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from elementsPage import *

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
site = os.getenv('SITE')
loginSucess = os.getenv('LOGIN_SUCESS')
passUser = os.getenv('PASSWORD')

def login(page):
    print("Acessei o site ✔")
    page.goto(site)
    print("Preenchi o usuário ✔")
    page.fill(usernameField,loginSucess)
    print("Preenchi a senha ✔")
    page.fill(passwordField,passUser)
    print("Cliquei no botão Logar ✔")
    page.click(loginButton)
    page.wait_for_load_state('networkidle')

def openAbout(page):
    print('Cliquei em "Sobre" ✔')
    page.click(aboutButton)
    page.click(closeButton)

def addItens(page):
    print('Adicionei a bolsa ao carrinho ✔')
    page.click(addToCartBackpack)
    print('Adicionei a bicicleta ao carrinho ✔')
    page.click(addToCartBikeLight)

    print('Cliquei no carrinho ✔')
    page.click(cartLink)

    print('Cliquei em checkout ✔')
    page.click(checkoutButton)

    # Preenche as informações de checkout
    print('Estou preenchendo as infos ...')
    page.fill(firstNameField, 'Renan')
    page.fill(lastNameField, 'Nascimento')
    page.fill(postalCodeField, '17000-000')
    print('Nome, último nome e CEP preenchidos ✔')

    page.click(continueButton)
    print('Cliquei em Continuar ✔')

    page.click(finishButton)
    print('Cliquei em Finish ✔')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=600)
    context = browser.new_context()
    page = context.new_page()

    login(page)
    openAbout(page)
    addItens(page)

    browser.close()
