import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import selectors

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
site = os.getenv('SITE')
loginSucess = os.getenv('LOGIN_SUCES')
passUser = os.getenv('PASSWORD')

def login(page):
    print("Acessei o site ✔")
    page.goto(site)
    print("Preenchi o usuário ✔")
    page.fill(selectors.usernameField, loginSucess)
    print("Preenchi a senha ✔")
    page.fill(selectors.passwordField, passUser)
    print("Cliquei no botão Logar ✔")
    page.click(selectors.loginButton)
    page.wait_for_load_state('networkidle')

def openAbout(page):
    print('Cliquei em "Sobre" ✔')
    page.click(selectors.aboutButton)
    page.click(selectors.closeButton)

def addItens(page):
    print('Adicionei a bolsa ao carrinho ✔')
    page.click(selectors.addToCartBackpack)
    print('Adicionei a bicicleta ao carrinho ✔')
    page.click(selectors.addToCartBikeLight)

    print('Cliquei no carrinho ✔')
    page.click(selectors.cartLink)

    print('Cliquei em checkout ✔')
    page.click(selectors.checkoutButton)

    # Preenche as informações de checkout
    print('Estou preenchendo as infos ...')
    page.fill(selectors.firstNameField, 'Cleitin')
    page.fill(selectors.lastNameField, 'Rei delas!')
    page.fill(selectors.postalCodeField, '7070-70dnv')
    print('Nome, último nome e CEP preenchidos ✔')

    page.click(selectors.continueButton)
    print('Cliquei em Continuar ✔')

    page.click(selectors.finishButton)
    print('Cliquei em Finish ✔')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    login(page)
    openAbout(page)
    addItens(page)

    browser.close()
