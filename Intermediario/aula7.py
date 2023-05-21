"""
    Exercicios com funções
    Crie uma Função que multiplica todos os argumentos
    não nomeados recebidos
    Retorne o total para uma variavel e mostre o valor
    da variavel
    
    Crie uma função fala se um número é par ou impar
    Retorne se o número é par ou impar
    
"""


def multiNumber(*args):
    
    total = 1 
    for number in args:        
        total *=number            
    return total


def evenOrOdd(number):
    if number % 2 == 0:
        return f'This Number Inform is Even'    
    return f'This Number Inform is Odd'        
        

total = multiNumber(1,2,4,5)        

print(1*2*4*5) 
print(total)

print(evenOrOdd(47))
