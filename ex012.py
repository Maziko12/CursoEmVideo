preço = float(input('Qual é o preço do produto?\nR: '))
desconto = preço / 100 * 5
print(f'O novo preço do produto é {desconto + preço:.0f}')