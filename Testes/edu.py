l = ('zero','um','dois', 'tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
l2 = 'vinte','trinta','quarenta','cinquenta','sessenta','oitenta','noventa'
while True:
    n = int(input('Digite um numero entre 0 e 100:'))
    if n < 20: 
        print(f'{n} por extenso fica assim: {l[n]}')
        break
    if 19< n < 100: 
        a = int(str(n)[0])-2
        b = int(str(n)[-1])
        if b==0:
            print(f'{n} por extenso fica assim: {l2[b]}')
        else:
            print(f'{n} por extenso fica assim: {l2[a]+" e "+l[b]}')
            break