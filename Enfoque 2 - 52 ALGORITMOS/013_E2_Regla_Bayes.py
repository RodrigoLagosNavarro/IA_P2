# ============================================================
# Enfoque 2: Regla de la Cadena (Probabilidad Conjunta)
# Autor: Rodrigo Lagos Navarro - 23110148 - Grupo 6E 2P
# ============================================================

# Este programa calcula la probabilidad de tener una enfermedad
# dado un resultado positivo en una prueba médica, aplicando la
# Regla de Bayes a probabilidades conocidas (teorema bayesiano).

# Probabilidades base
P_enfermedad = 0.01        # P(E)
P_prueba_pos_si_E = 0.90   # P(P | E)
P_prueba_neg_si_noE = 0.80 # P(N | ¬E)

# Complemento: no tener la enfermedad
P_no_enfermedad = 1 - P_enfermedad  # P(¬E)

# Probabilidad total de un resultado positivo: P(P)
P_prueba_pos_total = (P_prueba_pos_si_E * P_enfermedad) + \
                     ((1 - P_prueba_neg_si_noE) * P_no_enfermedad)

# Regla de Bayes: Probabilidad de tener la enfermedad dado positivo
P_enfermedad_dado_pos = (P_prueba_pos_si_E * P_enfermedad) / P_prueba_pos_total

print(f"La probabilidad de tener la enfermedad dado un resultado positivo es: {P_enfermedad_dado_pos:.2%}")
