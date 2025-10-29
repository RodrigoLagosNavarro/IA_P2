# ============================================================
# Enfoque 1: Valor de la informacion
# Autor: Rodrigo Lagos Navarro - Grupo 6E 2P
# ============================================================

# Este código calcula el valor de la información adicional,
# definido como la diferencia entre el valor esperado con la nueva información
# y el valor esperado previo a obtenerla.

class InformationValue:
    def __init__(self, prior_expected_value, new_expected_value):
        self.prior_expected_value = prior_expected_value  # Valor esperado sin información adicional
        self.new_expected_value = new_expected_value      # Valor esperado con información adicional

    def calculate_value(self):
        # Valor de la información = mejora en el valor esperado
        return self.new_expected_value - self.prior_expected_value

# Valores de ejemplo
prior_expected_value = 50  
new_expected_value = 70   

# Creación del objeto y cálculo del valor de la información
info_value = InformationValue(prior_expected_value, new_expected_value)
value = info_value.calculate_value()

print(f"El valor de la información es: {value}")
