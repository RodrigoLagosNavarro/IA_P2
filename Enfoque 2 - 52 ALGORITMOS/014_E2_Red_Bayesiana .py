# ============================================================
# Enfoque 2: Regla de la Cadena (Probabilidad Conjunta)
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este programa implementa una red bayesiana simple donde se
# almacenan probabilidades condicionales y se consultan desde código.

from collections import defaultdict  # Manejo de probabilidades

class RedBayesiana:
    def __init__(self):
        self.probabilidades = defaultdict(dict)  # Guarda P(A | B)

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        self.probabilidades[evento][dado_evento] = probabilidad

    def calcular_probabilidad(self, evento, dado_evento):
        return self.probabilidades[evento].get(dado_evento, None)

    def mostrar_probabilidades(self):
        for evento, condicionadas in self.probabilidades.items():
            for dado_evento, probabilidad in condicionadas.items():
                print(f"P({evento} | {dado_evento}) = {probabilidad}")

# Crear y configurar la red
red = RedBayesiana()
red.agregar_probabilidad('Emmanuel', 'Fernanda', 0.7)
red.agregar_probabilidad('Emiliano', 'Fernanda', 0.6)
red.agregar_probabilidad('Fernanda', 'Emiliano', 0.8)

# Consultar probabilidades
print("\nResultados de la Red Bayesiana:")
print(f"P(Emmanuel | Fernanda) = {red.calcular_probabilidad('Emmanuel', 'Fernanda')}")
print(f"P(Emiliano | Fernanda) = {red.calcular_probabilidad('Emiliano', 'Fernanda')}")

# Mostrar datos registrados
print("\nProbabilidades almacenadas:")
red.mostrar_probabilidades()
