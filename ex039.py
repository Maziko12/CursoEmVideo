# Crie um programa que leia a DataDeNascimento, e diga se vai se alistar, quando ou se já passou.
from datetime import date
pergunta = int(input('Qual é o seu ano de nascimento?\nR: '))
hoje = date.today().year
idade = hoje - pergunta
if idade == 18:
    print("Chegou a hora meu garotão! Vai ter que se alistar, e não tem desculpa kKKKKK")
elif idade >= 19:
    print("Você passou do tempo de ir rápido, a sua multa será de ~R$5,53!")
elif idade <= 17:
    print('Muito bem! Você ainda irá se alistar, mas falta um tempo. Boa sorte!')