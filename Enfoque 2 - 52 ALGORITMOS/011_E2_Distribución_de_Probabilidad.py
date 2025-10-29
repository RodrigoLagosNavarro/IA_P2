# ============================================================
# Enfoque 2: Distribución de Probabilidad
# Autor: Rodrigo Lagos Navarro - Grupo 6E 2P
# ============================================================

# Genera datos aleatorios con distribuciones normal y uniforme
# y grafica sus histogramas para comparar su comportamiento.

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de generación de datos
media = 0
desviacion_estandar = 1
n_datos = 1000

# Distribución normal
datos_normal = np.random.normal(loc=media, scale=desviacion_estandar, size=n_datos)

# Distribución uniforme
datos_uniforme = np.random.uniform(low=-3, high=3, size=n_datos)

# Visualización de las distribuciones
plt.figure(figsize=(14, 6))

# Histograma Normal
plt.subplot(1, 2, 1)
plt.hist(datos_normal, bins=30, edgecolor='black', density=True)
plt.title("Distribución Normal")
plt.xlabel("Valor")
plt.ylabel("Densidad de Frecuencia")

# Histograma Uniforme
plt.subplot(1, 2, 2)
plt.hist(datos_uniforme, bins=30, edgecolor='black', density=True)
plt.title("Distribución Uniforme")
plt.xlabel("Valor")
plt.ylabel("Densidad de Frecuencia")

plt.tight_layout()
plt.show()
