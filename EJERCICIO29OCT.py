import math

ventas = [100,120,150,200,300,450]
crecimiento = []

for i in range(1, len(ventas)):
    porcentaje = (ventas[i] - ventas[i - 1]) / ventas[i - 1] * 100
    crecimiento.append(porcentaje)

print("crecimiento porcentual:", crecimiento)

ventas_normalizadas = [math.log(v) for v in ventas]
print( "ventas normalizadas :", ventas_normalizadas)