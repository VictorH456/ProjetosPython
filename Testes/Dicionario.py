dic = {'nome':'Pedro',
       'idade':25,
       'casa':'popular'
       }

print(dic['nome'])
print(dic['idade'])
dic['sexo'] = 'M'
print(dic['sexo'])
print(dic['casa'])
print(dic.values())
print(dic.keys())
print(dic.items())
for k,v in dic.items(): print(f'O {k} é {v}')