# Constantes NÃO existem em python
# Para criar uma "constante", cria-se uma variável com todos os caracteres maiúsculos para sinalizar que ela não deve ter seu valor mudado

velocidade = 60
km = 90

RADAR = 60
LOCAL_1 = 100
RANGE_RADAR = 1

if(velocidade > RADAR): 
    print("Carro possui velocidade maior do que a do RADAR_1.")
    if(km <= (LOCAL_1 + RANGE_RADAR) and km >= (LOCAL_1 - RANGE_RADAR)): print("O carro foi multado")