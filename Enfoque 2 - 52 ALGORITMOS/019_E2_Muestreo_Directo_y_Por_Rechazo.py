# ============================================================
# Enfoque 2 - Muestreo Directo y por Rechazo
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este código implementa el muestreo por rechazo
# para generar muestras de una distribución objetivo usando
# una distribución propuesta más simple.

import numpy as np
import matplotlib.pyplot as plt

class MuestreoPorRechazo:
    def __init__(self, distribucion_objetivo, distribucion_propuesta):
        self.distribucion_objetivo = distribucion_objetivo
        self.distribucion_propuesta = distribucion_propuesta
    
    def muestreo(self, n):
        # Genera n muestras aceptadas según la regla de rechazo
        muestras = []
        for _ in range(n):
            x = self.distribucion_propuesta()          # Muestra de la distribución propuesta
            u = np.random.uniform(0, 1)               # Valor aleatorio para aceptación
            if u < self.distribucion_objetivo(x) / 0.5:  # Acepta si cumple con el criterio (0.5 normalización)
                muestras.append(x)
        return muestras

# Definir la distribución objetivo (normal centrada en 1)
def distribucion_objetivo(x):
    return 0.5 * np.exp(-0.5 * (x - 1) ** 2)

# Definir la distribución propuesta (uniforme)
def distribucion_propuesta():
    return np.random.uniform(-3, 5)

# Crear instancia de Muestreo por Rechazo
muestreo = MuestreoPorRechazo(distribucion_objetivo, distribucion_propuesta)

# Generar muestras
n_muestras = 1000
muestras = muestreo.muestreo(n_muestras)

# Visualizar resultados
plt.hist(muestras, bins=30, density=True, alpha=0.6, color='g', label='Muestras aceptadas')
x = np.linspace(-3, 5, 100)
plt.plot(x, distribucion_objetivo(x), label='Distribución objetivo', color='red')
plt.title('Muestreo por Rechazo')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.legend()
plt.show()
