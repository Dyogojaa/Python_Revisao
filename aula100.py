# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)



import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumentar os preços em 10%
novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] *= 1.1
    produto['preco'] = round(produto['preco'],2)
    

# Ordenar os produtos por nome decrescente (do maior para o menor)
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'], reverse=True)

# Ordenar os produtos por preço crescente (do menor para o maior)
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])

# Exibir os resultados
print("Novos Produtos:")
for produto in novos_produtos:
    print(produto)

print("\nProdutos Ordenados por Nome:")
for produto in produtos_ordenados_por_nome:
    print(produto)

print("\nProdutos Ordenados por Preço:")
for produto in produtos_ordenados_por_preco:
    print(produto)