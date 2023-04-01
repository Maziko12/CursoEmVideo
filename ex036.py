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
valorCasa = int(input('Qual é o preço da casa?\nR: '))
valorSalario = float(input('Qual é o seu salário?\nR: '))
tempoPagamento = int(input('Por quanto tempo em anos você quer pagar?\nR: ')).pu
# transformar int em string para operacionar
strvalorCasa = str(valorCasa)
strvalorSalario = str(valorSalario)
# Trabalhar nelas mais pra frente, para tirar a vírgula e pontuação
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
porcentagem = valorCasa / Meses * 100 / valorSalario
# Decidindo se o valor é aceitável (inferior á 30% ou não)
print('----------------')
print('Muito bem.')
print('----------------')
print('.')
time.sleep(3)
if porcentagem >= 31:
    time.sleep(3)
    print(f'Infelizmente, a margem de desconto no seu salário exigiu o limite de 30%, e foi {porcentagem}%.\nPor favor, escolha uma opção mais em conta na próxima!')
else:
    print(f'A sua compra poderá ser feita, pois descontará apenas {porcentagem}% do seu salário. A entrega chegará em poucos dias se aceitar agora.')
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