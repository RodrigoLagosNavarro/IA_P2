# ============================================================
# Enfoque 2: Incertidumbre
# Autor: Rodrigo Lagos Navarro - Grupo 6E 2P
# ============================================================

# Calcula y grafica la probabilidad de obtener cierto número de caras
# al lanzar una moneda varias veces, mostrando la distribución binomial.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Número total de lanzamientos de la moneda
n_lanzamientos = 10  

# Probabilidad de éxito en cada lanzamiento (cara)
probabilidad_exito = 0.5  

# Vector con todos los posibles números de éxitos: 0, 1, ..., 10
x = np.arange(0, n_lanzamientos + 1)

# Calcula la PMF (probabilidad de masa) de la distribución binomial
probabilidades = binom.pmf(x, n_lanzamientos, probabilidad_exito)

# Visualización de los resultados
plt.figure(figsize=(10, 6))
plt.stem(x, probabilidades, basefmt=" ", use_line_collection=True)  # Gráfico de tallo

# Configuración de etiquetas y título
plt.xlabel("Número de éxitos (caras)")
plt.ylabel("Probabilidad")
plt.title("Distribución Binomial: Probabilidad de obtener caras en lanzamientos de moneda")
plt.grid(True)  # Activar cuadrícula para facilitar lectura
plt.show()      # Mostrar gráfico
