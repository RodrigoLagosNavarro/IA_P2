# ============================================================
# Enfoque 2 - Inferencia por Enumeración
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este código implementa inferencia por enumeración sobre una
# Red Bayesiana simple usando probabilidades condicionales.

from collections import defaultdict

class RedBayesiana:
    def __init__(self):
        # Diccionario para almacenar las probabilidades condicionales
        self.probabilidades = defaultdict(dict)
    
    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        """
        Agrega P(evento | dado_evento) a la red bayesiana.
        """
        self.probabilidades[evento][dado_evento] = probabilidad

    def calcular_probabilidad(self, evento, dado_evento):
        """
        Devuelve P(evento | dado_evento) si existe en la red; si no, 0.0
        """
        return self.probabilidades[evento].get(dado_evento, 0.0)

    def inferencia_por_enumeracion(self, evento_objetivo, dado_evento, valores_dado_evento):
        """
        Calcula P(evento_objetivo | dado_evento) usando inferencia por enumeración.
        """
        probabilidad_total = 0.0
        for valor in valores_dado_evento:
            prob_evento = self.calcular_probabilidad(evento_objetivo, valor)
            prob_dado = self.calcular_probabilidad(dado_evento, valor)
            probabilidad_total += prob_evento * prob_dado
        return probabilidad_total

# Crear la red bayesiana
red = RedBayesiana()

# Agregar probabilidades condicionales
red.agregar_probabilidad('A', 'B', 0.9)
red.agregar_probabilidad('A', '¬B', 0.2)
red.agregar_probabilidad('B', 'C', 0.7)
red.agregar_probabilidad('B', '¬C', 0.4)

# Valores posibles del evento dado
valores_dado_evento = ['B', '¬B']

# Calcular P(A | B) usando inferencia por enumeración
probabilidad_A_dado_B = red.inferencia_por_enumeracion('A', 'B', valores_dado_evento)

print(f"La probabilidad P(A | B) es: {probabilidad_A_dado_B:.4f}")
