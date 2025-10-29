# ============================================================
# Enfoque 2: Manto de Markov (Cadena de Markov)
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este programa simula una Cadena de Markov usando una matriz
# de transición entre tres estados posibles A, B y C.

import numpy as np

class MantoDeMarkov:
    def __init__(self, estados, matriz_transicion):
        self.estados = estados
        self.matriz_transicion = matriz_transicion
    
    def simular(self, estado_inicial, pasos):
        estado_actual = estado_inicial
        secuencia = [estado_actual]

        for _ in range(pasos):
            estado_actual = np.random.choice(
                self.estados,
                p=self.matriz_transicion[estado_actual]
            )
            secuencia.append(estado_actual)
        
        return secuencia

# Estados posibles
estados = ['A', 'B', 'C']

# Matriz de transición P(Estado_siguiente | Estado_actual)
matriz_transicion = {
    'A': [0.1, 0.6, 0.3],
    'B': [0.4, 0.2, 0.4],
    'C': [0.3, 0.5, 0.2]
}

# Crear instancia
markov = MantoDeMarkov(estados, matriz_transicion)

# Simular desde A durante 10 pasos
resultado = markov.simular('A', 10)

print("Secuencia de estados:")
print(resultado)
