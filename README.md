# Programacion_lineal

El código de ejercicioPlineal.py responde al siguiente problema:

Una confiteria es famosa por sus dos especialidades de tartas: la tarta imperial y la tarta de lima, la tarta imperial requiere para su elaboracion medio kilo de azucar y 8 huevos y tiene un precio de venta de 10 euros, la tarta de lima necesita 1 kilo de azucar y 8 huevos, y tiene un precio de venta de 10 euros, en el almacen quedan 10kilos de azucar, y 120 huevos, a) que combinacinoes de especialidades se pueden hacer? plantea el problema y representa graficamente el conjunto de solucinoes, b) cuantas unidades de cada especialidad han de producirse para obtener el mayor ingreso por ventas

Este codigo comienza definiendo las variables necesarias para el problema: la cantidad máxima de azúcar y huevos disponibles, el precio de venta de cada tipo de tarta y la cantidad de azúcar y huevos requeridos para producir cada tipo de tarta.

A continuación, se utiliza un bucle for anidado para iterar a través de todas las combinaciones posibles de tartas imperiales y tartas de lima. Para cada combinación, se verifica si se cumplen las restricciones de recursos (es decir, si la cantidad de azúcar y huevos utilizados no supera la cantidad máxima disponible). Si se cumplen las restricciones, se calcula el ingreso total por la venta de esas tartas y se actualiza el valor máximo encontrado hasta el momento si el ingreso total es mayor.

Finalmente, se imprimen en la consola los valores óptimos encontrados: la cantidad de tartas imperiales y tartas de lima a producir y los ingresos totales máximos por la venta de esas tartas.
