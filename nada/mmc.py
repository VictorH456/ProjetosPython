numero1 = int(input("Digite um número inteiro: ")) #Entrada do numero 1
numero2 = int(input("Digite outro número inteiro: ")) #Entrada do numero 2

mmc = 1
divisor = 2  # Inicializa o divisor com 2, o menor número primo

#Laço onde caso qualquer um dos números seja maior que 1 irá continuar
while numero1 > 1 or numero2 > 1:
    #Condicional, que se algum dos dois forem divisiveis pelo nosso divisor e possuir resto 0,
    #ele multiplica o mmc pelo divisor 
    if numero1 % divisor == 0 or numero2 % divisor == 0:
        mmc *= divisor
        if numero1 % divisor == 0: #verifica se o resultado possui resto 0, se for ele divide o numero 1 pelo divisor
            numero1 //= divisor
        if numero2 % divisor == 0: # verifica se o resultado possui resto 0, se for ele divide o numero 2 pelo divisor
            numero2 //= divisor
    else: #caso nenhum dos numeros possua divisão inteira, soma +1 no divisor
        divisor += 1

#Printa o resultado
print(f"O mmc dos números fornecidos é {mmc}")
