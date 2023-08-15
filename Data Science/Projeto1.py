import os
while True:
    sinal = input("Digite uma operação: + , - , * , / ")
    if sinal == 'x' or sinal == 'X':
        sinal = '*'
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    
    print(f"{valor1} {sinal} {valor2} = {valor1 + valor2}")
    if input("Deseja fazer outra operação?").upper == 'N':
        break
    os.system("cls")