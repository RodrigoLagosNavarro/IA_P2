# ============================================================
# Enfoque 2 - Eliminación de Variables
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este código implementa el método de eliminación de variables
# para calcular probabilidades condicionadas en una Red Bayesiana.

from collections import defaultdict

class RedBayesiana:
    def __init__(self):
        # Diccionario para almacenar probabilidades condicionales
        self.probabilidades = defaultdict(dict)

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        # Agrega P(evento | dado_evento) a la red
        self.probabilidades[evento][dado_evento] = probabilidad

    def calcular_probabilidad(self, evento, evidencia, variable):
        # Calcula P(evento | variable) * P(evidencia | variable)
        if variable in self.probabilidades[evento]:
            return self.probabilidades[evento][variable] * self.probabilidades[evidencia][variable]
        else:
            return 0.0

    def eliminar_variable(self, evento_objetivo, evidencia, variables_a_eliminar):
        # Suma sobre todas las variables a eliminar para obtener P(evento_objetivo | evidencia)
        probabilidad_total = 0.0
        for valor in variables_a_eliminar:
            probabilidad_total += self.calcular_probabilidad(evento_objetivo, evidencia, valor)
        return probabilidad_total

# Crear la red bayesiana
red = RedBayesiana()

# Agregar probabilidades condicionales
red.agregar_probabilidad('A', 'B', 0.9)
red.agregar_probabilidad('A', '¬B', 0.2)
red.agregar_probabilidad('B', 'C', 0.7)
red.agregar_probabilidad('B', '¬C', 0.4)

# Calcular P(A | B) eliminando la variable oculta 'C'
variables_a_eliminar = ['C']
probabilidad_A_dado_B = red.eliminar_variable('A', 'B', variables_a_eliminar)

print(f"La probabilidad P(A | B) usando eliminación de variables es: {probabilidad_A_dado_B:.4f}")
