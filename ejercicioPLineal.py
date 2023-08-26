x_optimo =0
y_optimo =0
ingresos_maximos =0
max_tartas = max(int(10 /0.5), int(120 / 8))

def restriccion_azucar(x, y):
    return 0.5*x + y <= 10

def restriccion_huevos(x, y):
    return 8*x +8* y <= 120

def ingresos(x, y):
    return 8*x + 10*y
    
for x in range(max_tartas + 1):
    for y in range(max_tartas + 1):
        if restriccion_azucar(x, y) and restriccion_huevos(x, y):
            ingresos_actuales = ingresos(x, y)
            if ingresos_actuales > ingresos_maximos:
                x_optimo = x
                y_optimo = y
                ingresos_maximos = ingresos_actuales

print(f"el número optimo de tartas imperiales a producir es: {x_optimo}")
print(f"el número optimo de tartas de lima a producir es: {y_optimo}")
print(f"Los ingresos máximos por ventas son: {ingresos_maximos} $")
