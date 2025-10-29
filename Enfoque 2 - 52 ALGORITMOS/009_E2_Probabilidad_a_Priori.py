# ============================================================
# Enfoque 2: Probabilidad a Priori
# Autor: Rodrigo Lagos Navarro - Grupo 6E 2P
# ============================================================

# Calcula y grafica las probabilidades a priori de clases simuladas
# a partir de una muestra aleatoria de datos etiquetados.

import numpy as np                              # Para operaciones numéricas y generación de datos aleatorios
import matplotlib.pyplot as plt                 # Para crear gráficos
from collections import Counter                 # Para contar ocurrencias de elementos en una lista/array

# Fijar semilla para reproducibilidad
np.random.seed(42)                               

# Generar muestra aleatoria de etiquetas 'A' y 'B'
datos = np.random.choice(['A', 'B'],            # Etiquetas posibles
                         size=100,              # Tamaño de la muestra
                         p=[0.7, 0.3])         # Probabilidades de selección: P('A')=0.7, P('B')=0.3

# Contar cuántas veces aparece cada clase
conteo = Counter(datos)                          
total = len(datos)                               # Total de observaciones

# Calcular probabilidades a priori por clase
probabilidades_a_priori = {
    clase: conteo[clase] / total
    for clase in conteo
}

# Mostrar resultados en consola
print("Probabilidades a Priori:")
for clase, probabilidad in probabilidades_a_priori.items():
    print(f"Clase {clase}: {probabilidad:.2f}")

# Gráfico de barras de probabilidades a priori
plt.bar(probabilidades_a_priori.keys(),          # Clases en el eje x
        probabilidades_a_priori.values(),        # Altura de las barras = probabilidad a priori
        color=['blue', 'orange'])                # Colores opcionales
plt.xlabel('Clase')                              # Etiqueta eje x
plt.ylabel('Probabilidad a Priori')              # Etiqueta eje y
plt.title('Probabilidades a Priori de Clases Simuladas')  # Título del gráfico
plt.show()                                       # Mostrar gráfico

