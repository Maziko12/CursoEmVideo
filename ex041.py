from datetime import date
datNasc = int(input('Qual o seu ano de nascimento? '))
agora = date.today().year
idade = agora - datNasc
if idade == 9: 
    print(f'Você é um atleta Mirim, {idade} anos.')
elif idade == 14:
    print(f'Você é um atleta Infantil, {idade} anos.')
elif idade == 19:
    print(f'Você é um atleta Junior, {idade} anos.')
elif idade == 20:
    print(f'Você é um atleta Sênior, {idade} anos.')
elif idade > 25:
    print(f'Já que você já tem experiência, e tem mais que 20 anos, você é um Atleta Master.')
