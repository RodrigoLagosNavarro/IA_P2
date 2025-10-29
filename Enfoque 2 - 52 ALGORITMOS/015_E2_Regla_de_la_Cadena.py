# ============================================================
# Enfoque 2: Regla de la Cadena 
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este programa aplica la Regla de la Cadena para calcular
# probabilidades conjuntas usando probabilidades condicionales.

class ReglaCadena:
    def __init__(self):
        self.probabilidades = {}  # Guarda P(X | Y)

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        self.probabilidades[(evento, dado_evento)] = probabilidad

    def calcular_probabilidad_conjunta(self, *eventos):
        probabilidad = 1.0
        for i in range(len(eventos) - 1):
            actual = eventos[i]
            siguiente = eventos[i + 1]
            p = self.probabilidades.get((siguiente, actual))
            if p is None:
                return f"No definida: P({siguiente} | {actual})"
            probabilidad *= p
        
        # Multiplicamos por la probabilidad inicial P(A)
        probabilidad *= self.probabilidades.get((eventos[0], None), 1.0)
        return probabilidad

# Configurar probabilidades
regla = ReglaCadena()
regla.agregar_probabilidad('A', None, 0.5)  # P(A)
regla.agregar_probabilidad('B', 'A', 0.6)   # P(B | A)
regla.agregar_probabilidad('C', 'B', 0.7)   # P(C | B)

# Calcular P(A, B, C)
resultado = regla.calcular_probabilidad_conjunta('A', 'B', 'C')
print(f"P(A, B, C) = {resultado:.4f}")
