# ============================================================
# Enfoque 2: Probabilidad Condicionada y Normalización
# Autor: Rodrigo Lagos Navarro - Grupo 6E 2P
# ============================================================

# Calcula probabilidades P(A), P(B), probabilidad condicionada P(A|B)
# y normaliza las combinaciones posibles para que su suma sea 1.

import numpy as np
import pandas as pd

# Generación de datos aleatorios
np.random.seed(42)
data = {
    'Evento_A': np.random.choice([0, 1], size=100, p=[0.6, 0.4]),  # Evento A
    'Evento_B': np.random.choice([0, 1], size=100, p=[0.7, 0.3])   # Evento B
}
df = pd.DataFrame(data)

# Probabilidades simples P(A) y P(B)
p_a = df['Evento_A'].mean()
p_b = df['Evento_B'].mean()
print(f"P(A): {p_a:.2f}")
print(f"P(B): {p_b:.2f}")

# Probabilidad condicionada P(A|B)
df_ab = df[df['Evento_B'] == 1]  
p_a_dado_b = df_ab['Evento_A'].mean()
print(f"P(A | B): {p_a_dado_b:.2f}")

# Normalización de probabilidades conjuntas
probabilidades = np.array([
    p_a * p_b,           # A ∧ B
    p_a * (1 - p_b),     # A ∧ no B
    (1 - p_a) * p_b,     # no A ∧ B
    (1 - p_a) * (1 - p_b) # no A ∧ no B
])

prob_normalizadas = probabilidades / probabilidades.sum()

# Imprimir resultados normalizados
print("\nProbabilidades normalizadas:")
eventos = ['A ∧ B', 'A ∧ no B', 'no A ∧ B', 'no A ∧ no B']
for evento, prob in zip(eventos, prob_normalizadas):
    print(f"{evento}: {prob:.2f}")
