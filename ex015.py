Km = float(input('Quantos Km foram percorridos?\nR: '))
Dias = float(input('Quantos dias de tempo alugado?\nR: '))
Pague = (Km * 0.15) + (Dias * 60)
print(f'O preço final segundo os {Dias} dias de tempo alugado e {Km} Km/s rodados é de R${Pague:.2f}!')