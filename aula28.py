'''
    Exercicio 
    Peça ao usuario para digitar seu nome
    Peça ao usuario para digitar sua idade
    Se nome e idade forem digitados 
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém {ou não} espaços
            Seu nome tem {n} letras
            A Primeira letra do Seu nome é {letra}
            A ultima letra do seu nome é {letra}
    Se Nada for Digitado em nome ou idade
        exiba "Desculpe você deixou campos vazios
'''

nome  = input("Digite seu nome..: ")
idade = input("Digitre sua Idade..: ")

if len(nome) !=0 and  len(idade) !=0: # também poderia ser utilizado nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome Invertido é {nome[::-1]}")
    print(f" Se Nome contém {len(nome)} letras ")
    if nome.count(" ")>0 :  # Também poderia ser utilizado o ' ' in nome:
        Brancos = nome.count(" ")
        print(f" Se Nome contém o total {Brancos} de espaçoes em branco")
    else:
        print(f"Seu nome não contém espaços")
    print(f"A primeira letra do nome é {nome[0]}")
    print(f"A ultima letra do nome é {nome[-1]}")            
else:
    print(f"Desculpe você deixou campos vazios!")    
    
                
        
    