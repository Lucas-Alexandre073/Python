"""
CONSTANTE = "Variaveis" que nao vao mudar 
Muitas conficoes no mesmo if(ruim)
    <--- Contagem de complexidade(ruim)
"""
velocidade = 61 #velocidadeatual do carro 
local_carro = 101 #local que o carro esta na estrada

RADAR_1 = 60 #Velocidade maxima do radar 1 
LOCAL_1 = 100 #Local aonde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1

carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1: 
   
    print('Velocidade carro passou do radar 1')
    
if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
   
    print('Carro multado em radar 1')
    