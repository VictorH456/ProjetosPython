import datetime
def hora():
    if horas > 11 and horas < 18:
        print(f"São {horal}, Tenha uma boa tarde,{nome}!")
    elif horas > -1 and horas < 12:
        print(f"São {horal}, Tenha um bom dia,{nome}!")
    else:
        print(f"São {horal}, Tenha uma boa noite,{nome}!")
#A função "hora()" é responsável por imprimir a saudação de acordo com a hora atual
def nomes():
    try:
        nome = input("Por favor, digite um nome válido: ")
        while type(nome) != str:
            nome = input("Por favor, digite um nome válido: ")
    except TypeError:
        print("Erro: você deve digitar um nome válido.")
    return nome
#a função "nomes()" é responsável por validar e obter o nome do usuário.
horal = datetime.now().time()
horas = horal.hour
nome = nomes()
hora()
