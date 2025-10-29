# ============================================================
# Enfoque 2 - Ponderación de Verosimilitud
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este código implementa la ponderación de verosimilitud
# para generar muestras de una distribución objetivo y asignarles pesos
# según la probabilidad bajo un modelo definido.

import numpy as np
import matplotlib.pyplot as plt

class PonderacionDeVerosimilitud:
    def __init__(self, modelo_probabilidad):
        self.modelo_probabilidad = modelo_probabilidad
    
    def muestreo(self, n):
        # Generar muestras de la distribución propuesta (uniforme)
        muestras = np.random.uniform(0, 1, n)
        # Calcular verosimilitudes según el modelo
        verosimilitudes = self.modelo_probabilidad(muestras)
        # Normalizar verosimilitudes para obtener los pesos
        pesos = verosimilitudes / np.sum(verosimilitudes)
        return muestras, pesos

# Modelo de probabilidad: distribución normal centrada en 0.5
def modelo_probabilidad(x):
    return np.exp(-0.5 * (x - 0.5) ** 2)

# Crear instancia y generar muestras
n_muestras = 1000
ponderacion = PonderacionDeVerosimilitud(modelo_probabilidad)
muestras, pesos = ponderacion.muestreo(n_muestras)

# Visualización de los resultados
plt.scatter(muestras, pesos, alpha=0.5)
plt.title('Ponderación de Verosimilitud')
plt.xlabel('Muestras')
plt.ylabel('Pesos')
plt.grid()
plt.show()
