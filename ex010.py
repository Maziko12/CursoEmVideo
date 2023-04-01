import time
print('-=-=-=-=-' * 2, 'EXERCÍCIO 10', 2 * '-=-=-=-=-')
print('Olá! Seja bem vindo á demonstração do Exercício 10 do ==Curso em Vídeo em Python==!')
time.sleep(1)
dolarhoje = 5.17
print('---------------------------------------------------')
real = float(input('Me diga, quantos reais você tem na sua carteira.\nR: '))
dols = real / dolarhoje
print(f'Você pode comprar ${dols:.2f} dólares com o seu dinheiro!')