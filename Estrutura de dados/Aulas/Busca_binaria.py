def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2 #divisão int
        chute = lista[meio]
        
        # encontrou o item
        if chute == item:
            return meio
        if chute < item:
            inicio = meio + 1
        else:
            fim = meio - 1
                            
    # Item não existe no conjunto
    return None