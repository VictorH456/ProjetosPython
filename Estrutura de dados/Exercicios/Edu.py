def busca_binaria(lista, chave):
  posicoes = []
  inicio = 0
  fim = len(lista) - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == chave:
      posicoes.append(meio)
      inicio = meio + 1
    elif lista[meio] < chave:
      inicio = meio + 1
    else:
      fim = meio - 1
  return posicoes

lista = [2, 2, 5, 8, 23, 24, 32, 44, 56, 99]
chave = 2

posicoes = busca_binaria(lista, chave)

if posicoes:
  print(f"chave {chave} foi encontrada na lista nas posições {posicoes}.")
else:
  print(f"chave {chave} não foi encontrada na lista.")