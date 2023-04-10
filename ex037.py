print('Olá! Vamos descobrir como fica o seu número em outras bases?')
numberDecimal = int(input('Beleza! Qual será o seu número inteiro?\nR: '))
askingNumberType = str(input('Muito bem. Agora qual será a base de conversão?\nR: '))
# conversor para base numéricas (apenas para binário, hexa e octal!):
binaryBase = 2
octalBase = 8
decimalBase = 10
HexalBase = 16
def baseConvertor(decimalBase):
    if askingNumberType == "binário":
        return bin(decimalBase)
    elif askingNumberType == "octal":
        return oct(decimalBase)
    elif askingNumberType == "hexadecimal":
        return hex(decimalBase)
    else:
        return "Base numérica inválida"