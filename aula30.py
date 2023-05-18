"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim), quando mais estiver afastado da margem é muito ruim
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

#No Python as constantes por convenção é utilizado em letras maiusculas
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade >  RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1-RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_1) 

multar_carro_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1


if vel_carro_pass_radar_1:
    print(f'O Carro ultrapassou o Limite de Velocidade {RADAR_1} no Radar')
    
if carro_passou_radar_1:
    print(f'O Carro Passou {RADAR_1} no Radar')          
    
if multar_carro_radar_1:
        print(f'O Carro foi multado em {RADAR_1} no Radar')