# ============================================================
# Enfoque 2 - Monte Carlo para cadenas de Markov
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este código implementa un muestreador Monte Carlo para cadenas de Markov (MCMC)
# para generar muestras de una distribución objetivo usando el método de aceptación/rechazo.

import numpy as np
import matplotlib.pyplot as plt

class MCMCSampler:
    def __init__(self, modelo_probabilidad, estado_inicial, n_iteraciones):
        self.modelo_probabilidad = modelo_probabilidad
        self.estado_actual = estado_inicial
        self.n_iteraciones = n_iteraciones
        self.muestras = []

    def propuesto(self):
        # Proponer un nuevo estado mediante perturbación normal
        return np.random.normal(self.estado_actual, 0.5)

    def aceptar_rechazar(self, nuevo_estado):
        # Calcular razón de aceptación
        probabilidad_actual = self.modelo_probabilidad(self.estado_actual)
        probabilidad_nueva = self.modelo_probabilidad(nuevo_estado)
        razon_aceptacion = probabilidad_nueva / probabilidad_actual
        u = np.random.uniform(0, 1)
        return u < razon_aceptacion

    def muestrear(self):
        for _ in range(self.n_iteraciones):
            nuevo_estado = self.propuesto()
            if self.aceptar_rechazar(nuevo_estado):
                self.estado_actual = nuevo_estado
            self.muestras.append(self.estado_actual)

# Modelo de probabilidad: distribución normal centrada en 0
def modelo_probabilidad(x):
    return np.exp(-0.5 * (x - 0) ** 2)

# Parámetros del muestreador
estado_inicial = 5.0
n_iteraciones = 1000

# Crear instancia y generar muestras
mcmc = MCMCSampler(modelo_probabilidad, estado_inicial, n_iteraciones)
mcmc.muestrear()

# Visualización
plt.hist(mcmc.muestras, bins=30, density=True, alpha=0.6, color='g', label='Muestras MCMC')
x = np.linspace(-4, 4, 100)
plt.plot(x, modelo_probabilidad(x), label='Distribución objetivo', color='red')
plt.title('Muestreo MCMC')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.legend()
plt.grid()
plt.show()
