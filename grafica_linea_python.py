#...
#César Pardo - 23-marzo-2020
#Código de una gráfica en Python
#...

import math
import matplotlib.pyplot as plt
#Para este caso, importo el módulo numpy pero no lo utilizo, 
#se puede quitar si se quiere. 
import numpy as np

#Creo una lista de datos.
lista1 = [11,2,3,15,8,13,21,34]
#Me permite abrir una ventana y mostrar la gráfica
plt.ion()
#Me permite crear la gráfica con los datos de la lista 1
plt.plot(lista1)
