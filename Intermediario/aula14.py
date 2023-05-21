import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy() #Copia Rasa, Listas, Dicionarios dentro não serão copiados
d3 = copy.deepcopy() #Copia profunda, copia tudo incluindo os subníveis

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)