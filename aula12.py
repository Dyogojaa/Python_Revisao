nome = 'Dyogo Jose Aparecido de Almeida'
altura = 1.63
peso = 87
imc = peso / ( altura ** 2) #Calculo do IMC 


linha_1 = f"{nome} tem {altura:.2f} de altura" #Interpolação de String
linha_2 = f"pesa {peso} quilos e seu IMC é" #Interpolação de String
linha_3 = f"{imc:.2f}" #Interpolação de String

print(linha_1, sep=" ")
print(linha_2,  sep=" ")
print(linha_3)



