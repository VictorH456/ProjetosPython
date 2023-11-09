x = int(input('Digite um número inteiro:')) #quantos números serão fatorados.
for i in range(x):
    n = int(input('Digite um número inteiro:'))
    print("Número primo   Expoente")
    divisor = 2
    while n != 1:
        exp = 0
        while n%divisor == 0:
            exp = exp + 1
            n = n/divisor
        if exp != 0:
            print(divisor,exp)
        divisor = divisor + 1