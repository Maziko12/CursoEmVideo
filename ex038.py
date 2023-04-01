# Crie um programa que leia 2 números, e mostre qual deles é o maior, e se não tiver um maior, conte.
numeroUm = int(input('Qual é o primeiro número?\nR: '))
numeroDois = int(input('Qual é o segundo número?\nR: '))
print('Muito bem....')
if numeroUm > numeroDois:
    print(f'O número {numeroUm} é o maior.')
elif numeroUm == numeroDois:
    print('Ambos os números são iguais, não existe número maior!')
elif numeroDois > numeroUm:
    print(f'O número maior é o {numeroDois}!')
print('\nFim.')