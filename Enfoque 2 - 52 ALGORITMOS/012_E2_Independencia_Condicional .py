# ============================================================
# Enfoque 2: Independencia Condicional
# Autor: Rodrigo Lagos Navarro - Grupo 6E 2P
# ============================================================

# Simulación de tres eventos A, B y C con la misma probabilidad.
# Se calcula si A es independiente de B cuando se conoce C.

import numpy as np
import pandas as pd

# Generamos datos aleatorios
np.random.seed(42)
data = {
    'Evento_A': np.random.choice([0, 1], size=1000, p=[0.5, 0.5]),
    'Evento_B': np.random.choice([0, 1], size=1000, p=[0.5, 0.5]),
    'Evento_C': np.random.choice([0, 1], size=1000, p=[0.5, 0.5])
}
df = pd.DataFrame(data)

# Probabilidades individuales
p_a = df['Evento_A'].mean()
p_b = df['Evento_B'].mean()
p_c = df['Evento_C'].mean()

# Probabilidades conjuntas
p_a_b = (df['Evento_A'] & df['Evento_B']).mean()
p_a_c = (df['Evento_A'] & df['Evento_C']).mean()
p_b_c = (df['Evento_B'] & df['Evento_C']).mean()

# P(A | B y C): probabilidad de A sabiendo que B y C ocurrieron
subset_bc = df[(df['Evento_B'] == 1) & (df['Evento_C'] == 1)]
p_a_dado_b_y_c = subset_bc['Evento_A'].mean()

# Resultados
print(f"P(A): {p_a:.2f}")
print(f"P(B): {p_b:.2f}")
print(f"P(C): {p_c:.2f}")
print(f"P(A y B): {p_a_b:.2f}")
print(f"P(A y C): {p_a_c:.2f}")
print(f"P(B y C): {p_b_c:.2f}")
print(f"P(A | B y C): {p_a_dado_b_y_c:.2f}")

# Verificación de independencia condicional
independencia_condicional = np.isclose(p_a_dado_b_y_c, p_a_c)
print(f"¿A es condicionalmente independiente de B dado C? {'Sí' if independencia_condicional else 'No'}")
