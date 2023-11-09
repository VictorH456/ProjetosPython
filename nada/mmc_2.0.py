while True:
    #Variaveis
    mmc = 1
    lista_de_numeros_escolhidos = [] #Números que a pessoa vai digitar
    lista_dos_numeros_fatorados = [] #Resultado da fatoração
    lista_mmc = []
    
    #Quantidade de numeros para calcular o mmc
    quantidade_numeros = int(input("Digite a quantidade de numeros: "))
    
    #Adicionando os numeros na lista
    for i in range(quantidade_numeros):
        numero = int(input("Digite um numero inteiro: "))
        lista_de_numeros_escolhidos.append(numero)
    
    lista_fatoracao = [[] for _ in range(len(lista_de_numeros_escolhidos))]

    #Laço no range do tamanho da lista dos números escolhidos
    for i in range(len(lista_de_numeros_escolhidos)):
        n = lista_de_numeros_escolhidos[i] #n recebe os números escolhidos
        divisor = 2
        while n != 1:
            exp = 0
            while n%divisor == 0:
                exp = exp + 1
                n = n/divisor
            if exp != 0:
                lista_fatoracao[i].append(divisor)
                lista_fatoracao[i].append(exp)
                lista_temporaria = divisor**exp #Aqui inves de adicionar o divisor e expoente eu só elevo logo direto
                lista_dos_numeros_fatorados.append(lista_temporaria) #aqui eu uso append para adicionar na lista
                
            divisor = divisor + 1
    
    lista_dos_numeros_fatorados.sort(reverse = True) #metodo reverse que coloca a lista em ordem decrescente
   
    #Laço que roda enquanto o tamanho da lista dos numeros fatorados for maior que zero
    while len(lista_dos_numeros_fatorados) > 0:
        numero_atual = lista_dos_numeros_fatorados.pop(0) #uso o pop para remover o primeiro valor da lista(o maior valor, pois usei o reverse)
        lista_mmc.append(numero_atual) #Adiciona na lista que usaremos para calcular o mmc depois

        for i in range(len(lista_dos_numeros_fatorados)): #Outro laço só que ele serve para rodar toda a lista
            if numero_atual % lista_dos_numeros_fatorados[i] == 0: 
                # Se o numero atual que é o maior da lista for divisivel por qualquer outro eu adiciono None no lugar
                lista_dos_numeros_fatorados[i] = None
        # Remove todas as ocorrências do None
        while None in lista_dos_numeros_fatorados:
            lista_dos_numeros_fatorados.remove(None)

    #Laço para calcular mmc
    for i in lista_mmc:
        mmc *= i
    
    if quantidade_numeros == 2:
        #formula mdc = a*b/mmc
        mdc = lista_de_numeros_escolhidos[0]*lista_de_numeros_escolhidos[1] / mmc
    else:
        for i in range(len()):
            pass

    #area de print
    print("Quantidade:",quantidade_numeros)
    for i in range(len(lista_de_numeros_escolhidos)):
        print("número:", lista_de_numeros_escolhidos[i])
        for j in range(len(lista_fatoracao)):
            print(lista_fatoracao[i][j],lista_fatoracao[i][j+1])
    print("O mmc é:", mmc)
    print("O mdc é:", mdc)

    #if para parar o codigo
    if int(input("Digite 1 para sair: ")) == 1: #fecha o progama caso o numero digitado seja 1
        exit() 