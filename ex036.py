# Importação de Biblioteca tempo
import time
import string
# Apresentação do programa (bot atendedor)
print("""====================================================================
====================================================================
Caro usuário, devido ao servidor estar lotado de requisições, precisaremos 
que espere alguns segundos, por favor, seja paciente...=============
====================================================================""")
# Intervalo de tempo
print('.')
time.sleep(0.5)
print('.')
time.sleep(0.3)
print('.')
time.sleep(0.3)
print('.')
time.sleep(0.3)
# Atendente se apresentando!
print('Olá, tudo bem? Vamos começar com as perguntas então!')
time.sleep(3)
valorCasa = str(input('Qual é o preço da casa?\nR: '))
valorSalario = str(input('Qual é o seu salário?\nR: '))
tempoPagamento = int(input('Por quanto tempo em anos você quer pagar?\nR: '))
# transformar int em string para operacionar
if valorCasa and valorSalario == string.punctuation:
    valorCasa = string.punctuation(',', '.')
    ValorSalario = string.punctuation(',', '.')
# Trabalhar nelas mais pra frente, para tirar a vírgula e pontuação
intvalorCasa = int(valorCasa)
intvalorSalario = int(valorSalario)
# Cálculando a quantidade de mesês por ano eu terei
Meses = tempoPagamento * 12
# Dando um tempo para o usuário esperar...
print('.')
time.sleep(2)
print('Espere! Fazendo os cálculos...')
time.sleep(2)
time.sleep(0.5)
print('.')
time.sleep(0.6)
print('.')
time.sleep(0.9)
print('.')
time.sleep(1.5)
print('.')
time.sleep(1)
print('.')
time.sleep(0.5)
print('.')
# Descobrindo quantos % vou gastar por mês para pagar em X anos.
porcentagem = intvalorCasa / Meses * 100 / intvalorSalario
# Decidindo se o valor é aceitável (inferior á 30% ou não)
print('----------------')
print('Muito bem.')
print('----------------')
print('.')
time.sleep(3)
if porcentagem >= 31:
    time.sleep(3)
    print(f'Infelizmente, a margem de desconto no seu salário exigiu o limite de 30%, e foi {porcentagem:.2f}%.\nPor favor, escolha uma opção mais em conta na próxima!')
else:
    print(f'A sua compra poderá ser feita, pois descontará apenas {porcentagem:.2f}% do seu salário. A entrega chegará em poucos dias se aceitar agora.')
time.sleep(2.7)
asking = str(input('Deseja comprar?\nR: ')).lower()
if porcentagem <= 30:
    print('Até a próxima e volte sempre!')
    exit()
if asking == 'sim'.lower():
    time.sleep(1)
    print('Muito bem, a compra chegará em breve, obrigado pela preferência!')
elif asking in 'Sim Talvez Não'.lower():
    time.sleep(1)
    print('Entendo...boas compras e volte sempre!')
print('.')
time.sleep(3)
print('FIM!')
print('=========================')
#
import time
import os


def limpar():
    if os.name == 'nt': #Se for NT que dizer que e windows
        os.system('cls')
    else: # Linux/MacOS
        os.system('clear')

print("Caro usuário, devido ao servidor estar lotado de requisições, precisaremos que espere alguns segundos, por favor, seja paciente...")
time.sleep(1.5)
limpar()
print("Olá, tudo bem? Vamos começar com as perguntas então!")
time.sleep(1.5)

while True:
    try:
        valorCasa = float(input("Qual é o preço da casa?\nR: "))
        valorSalario = float(input("Qual é o seu salário?\nR: "))
        tempoPagamento = int(input("Por quanto tempo em anos você quer pagar?\nR: "))
        break
    except ValueError:
        print("Por favor, insira um valor numérico válido!")

meses = tempoPagamento * 12
porcentagem = (valorCasa / meses) * 100 / valorSalario

limpar()
time.sleep(1.5)
print("Espere! Fazendo os cálculos...")
time.sleep(2.5)
limpar()

if porcentagem >= 31:
    print(f"Infelizmente, a margem de desconto no seu salário exige o limite de 30%, e foi {porcentagem:.2f}%. Por favor, escolha uma opção mais em conta na próxima!")
    time.sleep(1)
    quit()
else:
    print(f"A sua compra poderá ser feita, pois descontará apenas {porcentagem:.2f}% do seu salário. A entrega chegará em poucos dias se aceitar agora.")

while True:
    asking = input("Deseja comprar? (sim/não)\nR: ").lower()
    if asking == "sim":
        print("Muito bem, a compra chegará em breve, obrigado pela preferência!")
        break
    elif asking == "não":
        print("Até a próxima e volte sempre!")
        break
    else:
        limpar()
        print("Por favor, escolha uma opção válida!")


time.sleep(1.5)
print("FIM!")