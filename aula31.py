"""
    Flag (Bandeira) - Marcar um Local
    Nome = Não Valor
    is e is not ou não é (Tipo, Valor, identidade)
    id = Identidade
"""

# v1 = 'a'
# v2 = 'b'

# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None


if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print("Não faça algo")                
    


if passou_no_if is None:
    print('Não passou no If')

if passou_no_if is not None:
    print('Passou no If')    