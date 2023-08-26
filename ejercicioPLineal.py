tartas_imperiales=0
ingresos_maximos=0
tartas_lima=0


def restriccion_azucar(x, y):
    return 0.5 * x + y <= 10

def restriccion_huevos(x, y):
    return 8 * x + 8 * y <= 120

def ingresos (x, y):
    return 8 * x + 10 * y
    
max_tartas= max(int(10 / 0.5), int(120 / 8))

for x in range(max_tartas + 1):
    for y in range(max_tartas + 1):
        if restriccion_azucar(x, y) and restriccion_huevos(x, y):
            ingresos_actuales = ingresos(x, y)
            if ingresos_actuales > ingresos_maximos:
                tartas_imperiales = x
                tartas_lima = y
                ingresos_maximos = ingresos_actuales

print("el número optimo de tartas imperiales a producir es: ",tartas_imperiales)
print("el número optimo de tartas de lima a producir es: ",tartas_lima)
print("Los ingresos máximos por ventas son: $",ingresos_maximos)
